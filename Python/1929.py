import sys, math
input = sys.stdin.readline
print = sys.stdout.write


def isPrime(x, y):
    for i in range(x, y+1):
        num = int(math.sqrt(i))
        for j in range(x):
            if j == 1 or j == 0:
                continue
            else:
                if (j % i) == 0 :
                    continue