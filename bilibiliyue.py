import datetime
import time
from loguru import logger
import requests
import urllib.parse
import utils
import re

def t_to_d(timestamp):
    return datetime.datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")


class BiliBili:
    def __init__(self, cookies) -> None:
        """
        初始化BiliBili类
        :param cookies: Cookie字符串，格式应为 name=value;name=value;...
        """
        self.cookies = self._parse_cookies(cookies)
        self.csrf_token = self._validate_and_get_csrf()
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/540.36 (KHTML, like Gecko)"
        }
        self.session = requests.Session()

    def _parse_cookies(self, cookie_str):
        """
        安全解析Cookie字符串
        :param cookie_str: 原始Cookie字符串
        :return: 解析后的Cookie字典
        """
        cookies = {}
        for cookie in cookie_str.split(';'):
            if '=' in cookie:
                # 使用partition比split更安全
                key, sep, value = cookie.strip().partition('=')
                if key and sep:
                    # 对特殊字符进行URL解码
                    cookies[key] = urllib.parse.unquote(value)
        return cookies

    def _validate_and_get_csrf(self):
        """
        验证Cookie有效性并获取CSRF token
        :return: 有效的CSRF token
        :raises ValueError: 当Cookie验证失败时抛出异常
        """
        required_fields = ['bili_jct', 'SESSDATA', 'DedeUserID']
        missing_fields = [field for field in required_fields if field not in self.cookies]
        
        if missing_fields:
            raise ValueError(
                f"缺少必要字段: {', '.join(missing_fields)}\n"
                "请确保:\n"
                "1. 使用最新版B站登录cookies\n"
                "2. cookies包含完整字段（推荐字段：bili_jct, SESSDATA, DedeUserID）\n"
                "3. cookie格式正确（name=value形式，多个字段用分号分隔）\n"
                f"当前可用字段: {', '.join(self.cookies.keys())}"
            )
        
        # 验证bili_jct格式（32位十六进制字符串）
        if not re.match(r'^[a-f0-9]{32}$', self.cookies['bili_jct']):
            raise ValueError(
                "bili_jct字段格式不正确，应为32位十六进制字符串\n"
                "示例：80bc5a08db34b2a3a705fb6b6f1641be"
            )
        
        return self.cookies['bili_jct']

    def bws_info(self):
        """
        获取预约信息
        :return: 解析后的数据或False
        """
        url = "https://api.bilibili.com/x/activity/bws/online/park/reserve/info"
        params = {
            "csrf": self.csrf_token,
            "reserve_date": "20250711,20250712,20250713"
        }
        
        try:
            response = self.session.get(url, headers=self.headers, cookies=self.cookies, params=params, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            if data.get('code') != 0:
                logger.error(f"❌ 接口请求失败: {data.get('message', '未知错误')}")
                return False
                
            return data.get('data', False)
        except requests.exceptions.RequestException as e:
            logger.error(f"⚠️ 网络请求失败: {str(e)}")
            return False

    def bws_do(self, ticket_no, inter_reserve_id):
        """
        执行预约操作
        :param ticket_no: 票号
        :param inter_reserve_id: 活动ID
        :return: 请求响应
        """
        url = "https://api.bilibili.com/x/activity/bws/online/park/reserve/do"
        data = {
            "ticket_no": ticket_no,
            "csrf": self.csrf_token,
            "inter_reserve_id": inter_reserve_id
        }
        
        try:
            response = self.session.post(url, headers=self.headers, cookies=self.cookies, data=data, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"⚠️ 预约请求失败: {str(e)}")
            return {"code": -1, "message": "请求失败"}

def main():
    print(
        '嘻嘻预约开始 \n\n'
    )

    try:
        cookie = utils.load()['cookie']
        fuck_bw = BiliBili(cookie)
        bws_info = fuck_bw.bws_info()

        if not bws_info:
            print('账号信息错误或异常，请检查 网络/账号/Cookies 再试，详细报错见上方 err。')
            return

        ticket_days = list(bws_info['user_reserve_info'].keys())
        ticket_id = {}
        reserve_dict = {}

        print("当前账号BW购票信息：")
        for row in ticket_days:
            ticket_id[row] = bws_info['user_ticket_info'][row]['ticket']
            print(
                f"{bws_info['user_ticket_info'][row]['screen_name']} | 票种：{bws_info['user_ticket_info'][row]['sku_name']} | 电子票号：{bws_info['user_ticket_info'][row]['ticket']}"
            )

        print('\n')
        for row in ticket_days:
            for reserve in bws_info['reserve_list'][row]:
                title = reserve['act_title'].replace('\n', '')
                reserve_dict[reserve['reserve_id']] = [title, reserve['act_begin_time'], reserve['reserve_begin_time']]
                print(
                    f"活动代码：{reserve['reserve_id']}  {title} 预约：{t_to_d(reserve['reserve_begin_time'])} 开始：{t_to_d(reserve['act_begin_time'])}"
                )
            print("\n")

        reserve_id_list = []
        in_id = input('输入活动代码（四位数字）ps:今年是三位：')

        if int(in_id) not in reserve_dict:
            print('选择不正确！')
            return

        reserve_id_list.append(int(in_id))
        print(f'{in_id}：{reserve_dict[int(in_id)][0]} 已选中\n')

        print('一次抢一个，如果觉得抢的少请自行多开。\n')
        
        for i in reserve_id_list:
            days = datetime.datetime.fromtimestamp(reserve_dict[i][1]).strftime("%Y%m%d")
            ticket_no = ticket_id[days]
            inter_reserve_id = i
            gap_time = 0
            
            while True:
                current_time = int(time.time())
                if current_time <= reserve_dict[i][2]:
                    if current_time > gap_time + 3 and gap_time + 30 < reserve_dict[i][2]:
                        gap_time = current_time
                        print(
                            f'等待开票……当前优先预约：{reserve_dict[i][0]} | 剩余：{reserve_dict[i][2] - current_time}秒'
                        )
                    time.sleep(0.1)
                    continue

                res = fuck_bw.bws_do(ticket_no, inter_reserve_id)
                print(f"预约结果请自行判断，你B状态码没文档：{res}")
                
                if res["code"] == 0:
                    print("预约成功")
                time.sleep(0.25)

    except Exception as e:
        logger.error(f"🚨 主程序异常: {str(e)}")
        print(f"程序异常退出: {str(e)}")

if __name__ == '__main__':
    main()