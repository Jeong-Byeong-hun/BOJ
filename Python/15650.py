from itertools import combinations

number, c = map(int, input().split(' '))

tempList = [i for i in range(1, number + 1)]

answer = list(combinations(tempList, c))

for i in answer:
    print(*i)
