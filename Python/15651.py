from itertools import product

number, c = map(int, input().split(' '))

tempList = [i for i in range(1, number + 1)]

answer = list(product(tempList, repeat=c))

for i in answer:
    print(*i)
