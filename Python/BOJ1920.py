n = int(input())
number = list(map(int, input().split(' ')))
m = int(input())
numList = list(map(int, input().split(' ')))

for i in numList:
    if i in number:
        print(1)
    else:
        print(0)
