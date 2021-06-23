from collections import deque

n, k = map(int, input().split(' '))
li = deque()
answer = []
for i in range(n):
    li.append(i + 1)

while len(li) != 0:
    li.rotate(- (k - 1))
    answer.append(li.popleft())

print("<", end='')
print(str(answer)[1:-1], end='')
print(">", end='')
