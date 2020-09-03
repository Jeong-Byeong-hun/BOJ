import sys
input = sys.stdin.readline
print = sys.stdout.write

li = []


def push(x):
    li.append(x)


def pop():
    if len(li) == 0:
        return -1
    else:
        return li.pop(0)


def size():
    return len(li)


def empty():
    if len(li) == 0:
        return 1
    else:
        return 0


def front():
    if len(li) == 0:
        return -1
    else:
        return li[0]


def back():
    if len(li) == 0:
        return -1
    else:
        return li[len(li)-1]


for i in range(int(input())):
    text = input()
    te = text.split()

    if te[0] == 'push':
        push(te[1])
    elif te[0] == 'pop':
        print(str(pop())+"\n")
    elif te[0] == 'size':
        print(str(size())+"\n")
    elif te[0] == 'empty':
        print(str(empty())+"\n")
    elif te[0] == 'front':
        print(str(front())+"\n")
    elif te[0] == 'back':
        print(str(back())+"\n")


