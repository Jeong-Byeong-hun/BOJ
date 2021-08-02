remote = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
answer = int(input())
wrongNum = int(input())
number = list(map(int, input().split(' ')))
initNum = 100
for i in number:
    remote.remove(i)

print(remote)
