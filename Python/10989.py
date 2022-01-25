import sys

n = int(sys.stdin.readline())
li = [0] * 10001

for i in range(0, n):
    m = int(sys.stdin.readline())
    li[m] += 1

for i in range(1, 10001):
    if li[i] != 0:
        for j in range(li[i]):
            print(i)

