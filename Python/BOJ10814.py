from operator import itemgetter

n = int(input())
li = []
for i in range(n):
    m, n = input().split(' ')
    li.append((int(m), n, i))

temp = sorted(li, key=itemgetter(0, 2))

for i in temp:
    print(str(i[0]) + ' ' + i[1])
