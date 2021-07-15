from itertools import combinations_with_replacement

number, c = map(int, input().split(' '))

tempList = [i for i in range(1, number + 1)]

answer = list(combinations_with_replacement(tempList, c))

for i in answer:
    print(*i)
