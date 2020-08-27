import sys
n,m,k = map(int, sys.stdin.readline().split(' '))
li = []

for i in range(int(n)):
    temp = int(sys.stdin.readline())
    li.append(temp)

for i in range(m+k):
    a, b, c = map(int, sys.stdin.readline().split(' '))
    if a == 1 :
        li[b-1] = c
    elif a == 2 :
        print(sum(li[b-1:c]))
