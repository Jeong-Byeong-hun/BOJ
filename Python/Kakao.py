# 메뉴 리뉴얼 카카오 2021 블라인드
# 레스토랑을 운영하던 스카피는 코로나19로 인한 불경기를 극복하고자 메뉴를 새로 구성하려고 고민하고 있습니다.
# 기존에는 단품으로만 제공하던 메뉴를 조합해서 코스요리 형태로 재구성해서 새로운 메뉴를 제공하기로 결정했습니다.
# 어떤 단품메뉴들을 조합해서 코스요리 메뉴로 구성하면 좋을 지 고민하던
# "스카피"는 이전에 각 손님들이 주문할 때
# 가장 많이 함께 주문한 단품메뉴들을 코스요리 메뉴로 구성하기로 했습니다.
# 단, 코스요리 메뉴는 최소 2가지 이상의 단품메뉴로 구성하려고 합니다.
# 또한, 최소 2명 이상의 손님으로부터 주문된 단품메뉴 조합에 대해서만 코스요리 메뉴 후보에 포함하기로 했습니다.
#
# 예를 들어, 손님 6명이 주문한 단품메뉴들의 조합이 다음과 같다면,
# (각 손님은 단품메뉴를 2개 이상 주문해야 하며, 각 단품메뉴는 A ~ Z의 알파벳 대문자로 표기합니다.)

# orders 배열의 크기는 2 이상 20 이하입니다.
# orders 배열의 각 원소는 크기가 2 이상 10 이하인 문자열입니다.
# 각 문자열은 알파벳 대문자로만 이루어져 있습니다.
# 각 문자열에는 같은 알파벳이 중복해서 들어있지 않습니다.
# course 배열의 크기는 1 이상 10 이하입니다.
# course 배열의 각 원소는 2 이상 10 이하인 자연수가 오름차순으로 정렬되어 있습니다.
# course 배열에는 같은 값이 중복해서 들어있지 않습니다.
# 정답은 각 코스요리 메뉴의 구성을 문자열 형식으로 배열에 담아 사전 순으로 오름차순 정렬해서 return 해주세요.
# 배열의 각 원소에 저장된 문자열 또한 알파벳 오름차순으로 정렬되어야 합니다.
# 만약 가장 많이 함께 주문된 메뉴 구성이 여러 개라면, 모두 배열에 담아 return 하면 됩니다.
# orders와 course 매개변수는 return 하는 배열의 길이가 1 이상이 되도록 주어집니다.

import re
from collections import Counter
from itertools import combinations


def KakaoMenu(orders, course):
    answer = []

    for c in course:
        temp = []
        for o in orders:
            combi = combinations(sorted(o), c)
            temp += combi

        counter = Counter(temp)

        if len(counter) != 0 and max(counter.values()) > 1:
            for f in counter:
                if counter[f] == max(counter.values()):
                    answer += [''.join(f)]

    answer.sort()

    return answer


# 효용성 테스트 필요

def solution(info, query):
    answer = []
    for i in query:
        answerCheck = 0
        temp = i.replace("and", "").split(" ")

        while '' in temp:
            temp.remove('')
        # print(temp)

        for j in info:
            j = j.split(" ")
            check = 0
            for k in range(len(j)):
                if k == 4:
                    if int(j[k]) >= int(temp[k]):
                        check += 1
                    break
                if j[k] in temp:
                    # print(j[k])
                    # print("있음")
                    check += 1
                elif temp[k] == '-':
                    check += 1
                else:
                    break
            # print(j)
            if check == 5:
                # print(temp)
                # print(j)
                answerCheck += 1
        answer.append(answerCheck)

    return answer


info1 = ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
         "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"]
query1 = ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
          "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
          "- and - and - and - 150"]


# print(solution(info1, query1))

# 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
# 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
# 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
# 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
# 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
# 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
#      만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
# 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.


def createSolution(new_id):
    answer = ''
    new_id = new_id.lower()

    for word in new_id:
        if word.isalnum() or word in '-_.':
            answer += word

    while '..' in answer:
        answer = answer.replace("..", ".")

    if answer[0] == '.':
        answer = answer[1:]

    if len(answer) > 1:
        if answer[-1] == '.':
            answer = answer[:-1]

    if len(answer) == 0:
        answer = 'a'

    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]



    while len(answer) < 3:
        answer = answer + answer[-1]
    print(answer)
    return answer


# createSolution("...!@BaT#*..y.abcdefghijklm")
# createSolution("z-+.^.")
createSolution("=.=")
# createSolution("123_.def")
# createSolution("abcdefghijklmn.p")
