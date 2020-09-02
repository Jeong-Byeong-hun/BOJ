import math

def staryear(num):
    s = int(math.sqrt(num))
    cnt = (s * 2) - 1

    if s**2 == num:
        return cnt
    elif s ** 2 + s < num :
        cnt += 2

    elif s ** 2 + s >= num :
        cnt += 1

    return cnt


for i in range(int(input())):
    x, y = map(int,input().split(' '))
    s = y - x
    print(staryear(s))

