import sys
input = sys.stdin.readline
print = sys.stdout.write


def getParent(parent, x):
    if x == parent[x]:
        return x
    parent[x] = getParent(parent,parent[x])
    return parent[x]


def union(parent, x, y):
    x = getParent(parent, x)
    y = getParent(parent, y)

    if x < y :
        parent[y] = x
    else:
        parent[x] = y



city = int(input())

testcase = int(input())

parent = [int(i) for i in range(city + 1)]

now_city = 1
for i in range(city):
    city_list = list(map(int,input().split()))
    for i in range(len(city_list)):
        if city_list[i] == 1:
            union(parent,now_city, i+1)
    now_city += 1

city_union = list(map(int, input().split(' ')))

root = getParent(parent, city_union[0])
flag = True

for i in city_union:
    if root != getParent(parent, i):
        flag = False
        break

if flag:
    print('YES')
else:
    print('NO')