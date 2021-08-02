import math


def isPrime(testNum):
    for j in range(2, int(math.sqrt(testNum)) + 1):
        if testNum % j == 0:
            return False
    return True


m, n = map(int, input().split(' '))

for i in range(m, n + 1):
    if i == 1:
        continue
    if i == 2:
        print(2)
        continue
    if isPrime(i):
        print(i)

