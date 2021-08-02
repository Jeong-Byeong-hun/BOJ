def solution(answers):
    answer = []

    answer = math_answer(answers)

    return answer


def math_answer(answer_list):
    one_answer = [1, 2, 3, 4, 5]
    two_answer = [2, 1, 2, 3, 2, 4, 2, 5]
    three_answer = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    answer1 = 0
    answer2 = 0
    answer3 = 0

    for i in range(len(answer_list)):
        if answer_list[i] == one_answer[i % 5]:
            answer1 += 1
        if answer_list[i] == two_answer[i % 8]:
            answer2 += 1
        if answer_list[i] == three_answer[i % 10]:
            answer3 += 1

    answer_cnt = [answer1, answer2, answer3]
    answer_temp = []

    for person, score in enumerate(answer_cnt):
        if score == max(answer_cnt): answer_temp.append(person + 1)

    return answer_temp


print(solution([1, 3, 2, 4, 2]))
