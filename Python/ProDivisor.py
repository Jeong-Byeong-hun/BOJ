import math

def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        if math.sqrt(i).is_integer():
            answer = answer - i
        else:
            answer = answer + i

    return answer

