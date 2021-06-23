from collections import deque

num = int(input())
li = deque()
for i in range(num):
    li.append(i + 1)

while len(li) > 1:
    li.popleft()
    getNum = li.popleft()
    li.append(getNum)

print(li[0])
