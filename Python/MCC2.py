def solution(s):
    answer = 0
    if not isPossible(s):
        return 0

    for i in range(len(s)):
        list1 = []
        checkCount = 0

        for text in s:
            checkCount += 1
            if text == '[' or text == '{' or text == '(':
                list1.append(text)
            else:
                if len(list1) != 0:
                    tempStr = list1.pop()
                    if tempStr == '[' and text == ']':
                        continue
                    elif tempStr == '{' and text == '}':
                        continue
                    elif tempStr == '(' and text == ')':
                        continue
                    else:
                        list1.insert(0, 0)
                        break
                else:
                    list1.insert(0, 0)
                    break
        if len(list1) == 0:
            answer += 1
        s = sortList(s)
    return answer


def isPossible(s):
    tempNum = 0
    for i in range(len(s)):
        if s[i] == '[' or s[i] == '{' or s[i] == '(':
            tempNum += 1
        else:
            tempNum -= 1

    if tempNum != 0:
        return False

    return True


def sortList(s):
    temp = s[0]
    tes = ""
    for i in range(1, len(s)):
        tes += s[i]

    tes += temp
    return tes


testCase = "}}}"

print(solution(testCase))



