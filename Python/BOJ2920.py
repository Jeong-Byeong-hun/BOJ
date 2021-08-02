number = list(map(int, input().split(' ')))
ascList = [1, 2, 3, 4, 5, 6, 7, 8]
descList = [8, 7, 6, 5, 4, 3, 2, 1]

cntList = [0, 0]

for i in range(len(number)):
    if number[i] == ascList[i]:
        cntList[0] += 1
    if number[i] == descList[i]:
        cntList[1] += 1

answer = ''

if cntList[0] == 8:
    answer = 'ascending'
elif cntList[1] == 8:
    answer = 'descending'
else:
    answer = 'mixed'

print(answer)
