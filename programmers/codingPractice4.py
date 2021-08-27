tab = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
       "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
       "GAME C++ C# JAVASCRIPT C JAVA"]

lang = ["JAVA", "JAVASCRIPT"]

prefer = [7, 5]


def solution(table, languages, preference):
    answer = ''
    scoreList = []
    for i in range(len(table)):
        score = 0
        tempList = table[i].split(" ")
        tempList = tempList[::-1]
        for j in range(len(languages)):
            try:
                # print(languages[j])
                # print(tempList)
                preferScore = tempList.index(languages[j])
                # print(preferScore)
                preferScore += 1

                score += preferScore * preference[j]
                # print("score = " + str(score))
            except ValueError:
                continue

        scoreList.append((score, tempList[5]))

    scoreList.sort(key=lambda x: (-x[0], x[1]))

    answer = scoreList[0][1]

    return answer


print(solution(tab, lang, prefer))
