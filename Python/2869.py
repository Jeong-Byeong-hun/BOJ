import math

a, b ,v = map(int, input().split(' '))

top = v - b
dis = a - b
ans = top / dis

print(math.ceil(ans))