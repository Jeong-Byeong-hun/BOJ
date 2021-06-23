# 1	6개 번호가 모두 일치
# 2	5개 번호가 일치
# 3	4개 번호가 일치
# 4	3개 번호가 일치
# 5	2개 번호가 일치
# 6(낙첨)	그 외

def solution(lottos, win_nums):
    cnt = 0
    rank = 7

    for i in lottos:
        if i in win_nums:
            cnt = cnt + 1

    answer = [rank - cnt - lottos.count(0), rank - cnt]

    if answer[0] == 7:
        answer[0] = 6

    if answer[1] == 7:
        answer[1] = 6

    return answer


lotto = [32, 11, 21, 33, 5, 1]
wins = [31, 10, 45, 1, 6, 19]

solution(lotto, wins)
