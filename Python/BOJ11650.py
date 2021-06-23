from operator import itemgetter

n = int(input())
li = []
for i in range(n):
    p, q = map(int, input().split(' '))
    li.append([p, q])

li = sorted(li, key=itemgetter(0, 1))

for i in li:
    print(str(i[0]) + " " + str(i[1]))
