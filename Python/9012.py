for i in range(int(input())):
    text = input()
    li = []
    for i in text:
        if i == '(':
            li.append(i)
        else:
            if len(li) != 0:
                li.pop()
            else:
                li.append('0')
                break

    if len(li) == 0:
        print('YES')
    else:
        print('NO')