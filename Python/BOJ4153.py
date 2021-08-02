while True:
    tripleList = list(map(int, input().split(' ')))
    if tripleList[0] == 0:
        break
    tripleList.sort()
    a = tripleList[0] ** 2
    b = tripleList[1] ** 2
    c = tripleList[2] ** 2

    if (a + b) == c:
        print('right')
    else:
        print('wrong')

