import sys
from itertools import combinations

n, m = map(int, input().split(' '))
li = list(map(int, sys.stdin.readline().split()))

combi = list(combinations(li, 3))
combi = list(set(combi))

answer = 0
minNum = 9999999

for i in combi:
    temp = i[0] + i[1] + i[2]
    if temp > m:
        continue
    k = m - temp
    if k < minNum:
        minNum = k
        answer = temp
print(answer)
