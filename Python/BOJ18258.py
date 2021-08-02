que = []
number = int(input())

for i in range(number):
    text = input().split(' ')

    if text[0] == 'push':
        que.append(int(text[1]))
        print(str(que[0]))

    if text[0] == 'front':
        print(str(que[0]))
        if len(que) < 1:
            print(str(que[0]))
        else:
            print(str(-1))

    if text[0] == 'back':
        if len(que) != 0:
            print(str(que[len(que) - 1]))
        else:
            print(str(-1))

    if text[0] == 'size':
        print(str(len(que)))

    if text[0] == 'empty':
        if len(que) != 0:
            print(str(1))
        else:
            print(str(-1))

    if text[0] == 'pop':
        if len(que) != 0:
            print(str(que.pop(0)))
        else:
            print(str(-1))
