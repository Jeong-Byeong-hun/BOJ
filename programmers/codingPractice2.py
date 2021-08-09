# 자기 자신을 평가한 점수가 유일한 최고점 또는 유일한 최저점이라면 그 점수는 제외하고 평균을 구합니다.
# 최고점이나 최저점인데 동점인 경우는 제외


def solution(scores):
    answer = ''
    for i in range(len(scores)):
        tList = []
        for j in range(len(scores)):
            print(scores[j][i])
            tList.append(scores[j][i])

        print("======================")
        mylist = judge(tList, i)
        print(sum(mylist))
        print(len(mylist))
        avg = sum(mylist) / len(mylist)
        print(avg)
        answer += calculator(avg)
        print("======================")
    print(answer)
    return answer


def calculator(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 80:
        return 'B'
    elif avg >= 70:
        return 'C'
    elif avg >= 50:
        return 'D'
    else:
        return 'F'


def judge(scores, num):
    # num = 내가 점수를 준 index
    myScore = scores[num]

    print(scores.pop(num))
    print(scores)
    print(max(scores))
    if max(scores) >= myScore >= min(scores):
        scores.append(myScore)

    return scores


temp = [[100, 90, 98, 88, 65], [50, 45, 99, 85, 77], [47, 88, 95, 80, 67], [61, 57, 100, 80, 65], [24, 90, 94, 75, 65]]

solution(temp)
