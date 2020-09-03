import sys
input = sys.stdin.readline
print = sys.stdout.write

li = []


def push_back(x):
    li.append(x)


def push_front(x):
    li.insert(0, x)


def pop_front():
    if len(li) == 0:
        return -1
    else:
        return li.pop(0)


def pop_back():
    if len(li) == 0:
        return -1
    else:
        return li.pop()


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

    if te[0] == 'push_back':
        push_back(te[1])
    elif te[0] == 'push_front':
        push_front(te[1])
    elif te[0] == 'pop_front':
        print(str(pop_front())+"\n")
    elif te[0] == 'pop_back':
        print(str(pop_back()) + "\n")
    elif te[0] == 'size':
        print(str(size())+"\n")
    elif te[0] == 'empty':
        print(str(empty())+"\n")
    elif te[0] == 'front':
        print(str(front())+"\n")
    elif te[0] == 'back':
        print(str(back())+"\n")


