num = int(input())
start = 1


def hap(n):
    temp = n + sum(map(int, list(str(n))))
    if temp == num :
        return n

    elif n > num :
        return 0
    else:
        return n


while hap(start) + sum(map(int, list(str(start)))) != num:

    if hap(start) == 0:
        start = 0
        break
    else:
        start += 1

print(start)



