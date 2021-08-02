# 제한사항
# 1 ≤ s의 길이 ≤ 50
# s가 "zero" 또는 "0"으로 시작하는 경우는 주어지지 않습니다.
# return 값이 1 이상 2,000,000,000 이하의 정수가 되는 올바른 입력만 s로 주어집니다.


# 0	zero
# 1	one
# 2	two
# 3	three
# 4	four
# 5	five
# 6	six
# 7	seven
# 8	eight
# 9	nine

def solution(s):
    answer = ""

    while not s.isdigit():
        s = s.replace("zero", "0")

        s = s.replace("one", "1")

        s = s.replace("two", "2")

        s = s.replace("three", "3")

        s = s.replace("four", "4")

        s = s.replace("five", "5")

        s = s.replace("six", "6")

        s = s.replace("seven", "7")

        s = s.replace("eight", "8")

        s = s.replace("nine", "9")


    return int(s)

solution("2three45sixseven")
