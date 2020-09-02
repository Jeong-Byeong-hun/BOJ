cnt = 0
li = []


def hanoi(n,f,s,t):
    global cnt
    if n == 1:
        cnt += 1
        li.append([f, t])
    else:
        hanoi(n-1,f,t,s)
        hanoi(1,f,s,t)
        hanoi(n-1,s,f,t)


k = int(input())


hanoi(k, 1, 2, 3)

print(cnt)
for i in li:
    print(i[0], i[1])