A = input('Enter list:')
ls =[]
for i in A:
    try:
        if i.isalnum():
            ls.append(int(i))
    except ValueError:
        pass

def CountZeros(A):
    if A == '':
        return 0
    counter = 0
    for i in A:
        if (i == 0):
            counter += 1
    return counter

zeros_A = CountZeros(ls)
print(zeros_A)