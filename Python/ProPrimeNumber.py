from itertools import combinations
import math


def solution(nums):
    answer = 0

    test = list(combinations(num, 3))

    for i in test:
        temp_number = sum(i)
        if isPrime(temp_number):
            cnt = cnt + 1

    return answer


def isPrime(testNum):
    for j in range(2, int(math.sqrt(testNum)) + 1):
        if testNum % j == 0:
            return False
    return True


num = [1, 2, 7, 6, 4]
