def solution(numbers):
    allNumber = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    for i in numbers:
        allNumber.remove(i)

    answer = sum(allNumber)

    return answer


temp = [1, 2, 3, 4, 6, 7, 8, 0]
solution(temp)
