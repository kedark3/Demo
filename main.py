import requests
import csv
import time

# Your D-ID API key
api_key = 'YOUR_API_KEY'

# Read questions from a CSV file
with open('Questionsdemocsv.csv', mode='r', newline='') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        job_title = row['Job Title']
        question = row['Questions']
        q_no = row['Q no.']

        # Create a talk for each question
        create_url = "https://api.d-id.com/talks"
        create_payload = {
            "script": {
                "type": "text",
                "subtitles": False,
                "provider": {
                    "type": "microsoft",
                    "voice_id": "en-IN-NeerjaNeural"
                },
                "ssml": "false",
                "input": question
            },
            "config": {
                "fluent": "false",
                "pad_audio": "0.0",
                "stitch": "true"
            },
            "name": f"{job_title}_Q{q_no}",
            "source_url": "https://create-images-results.d-id.com/DefaultPresenters/Fatha_f/image.png"
        }
        create_headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "authorization": f"Basic {api_key}"
        }
        create_response = requests.post(create_url, json=create_payload, headers=create_headers)

        if create_response.status_code == 201:
            talk_id = create_response.json().get('id')
            print(f"Talk created successfully for question: {question}, Talk ID: {talk_id}")

            # Wait and periodically check for the result URL
            max_attempts = 3
            attempts = 0
            while attempts < max_attempts:
                time.sleep(20)  # Wait for 30 seconds
                attempts += 1

            # Download the video using the talk ID
            download_url = f"https://api.d-id.com/talks/{talk_id}"
            download_headers = {
                "accept": "application/json",
                "authorization": f"Basic {api_key}"
            }
            download_response = requests.get(download_url, headers=download_headers)

            if download_response.status_code == 200:
                talk_details = download_response.json()
                result_url = talk_details.get("result_url")

                if result_url:
                    # Specify a custom name for the downloaded file
                    custom_filename = f"{job_title}_Q{q_no}.mp4"

                    # Download the file and save it with the custom name
                    with open(custom_filename, 'wb') as file:
                        video_data = requests.get(result_url)
                        file.write(video_data.content)

                    print(f"Video for question '{question}' downloaded as '{custom_filename}'")
                else:
                    print("Result URL not found in the response.")
            else:
                print(f"Error: {download_response.status_code} - {download_response.text}")
        else:
            print(f"Error: {create_response.status_code} - {create_response.text}")
