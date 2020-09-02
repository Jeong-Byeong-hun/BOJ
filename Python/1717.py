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


def find(parent, x, y):
    x = getParent(parent, x)
    y = getParent(parent, y)
    if x == y:
        print("YES\n")
    else:
        print("NO\n")


n, m = map(int, input().split(' '))

parent = [int(i) for i in range(n+1)]

for i in range(m):
    choose, a , b = map(int, input().split(' '))

    if choose == 0:
        union(parent, a, b)
    else:
        find(parent, a ,b)