from itertools import permutations

number, c = map(int, input().split(' '))

tempList = [i for i in range(1, number + 1)]

answer = list(permutations(tempList, c))

for i in answer:
    s = ""
    for j in i:
        s += str(j) + " "

    print(s.rstrip())
