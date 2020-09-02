while True:
    li = []

    text = input()
    if text == ".":
        break
    for i in text:
        if i == "(":
            li.append(i)
        elif i == ")" :
            if len(li) != 0 :
                temp = li.pop()
                if temp == "(":
                    continue
                else:
                    li.append('0')
            else :
                li.append('0')
                break
        elif i =="[":
            li.append(i)
        elif i == "]":
            if len(li) != 0:
                temp = li.pop()
                if temp == "[":
                    continue
                else:
                    li.append('0')
            else :
                li.append('0')
                break

    if len(li) == 0 :
        print("yes")
    else:
        print("no")

