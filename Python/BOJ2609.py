import math

n, m = map(int, input().split(' '))

print(math.gcd(n, m))
lcmNum = (n * m) / math.gcd(n, m)
print(int(lcmNum))
