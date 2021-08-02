from operator import itemgetter

n = int(input())

li = []
for i in range(n):
    temp = input()
    li.append((temp, len(temp)))

li = list(set(li))

for i in sorted(li, key=itemgetter(1, 0)):
    print(i[0])
