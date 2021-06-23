from itertools import permutations


def solution(numbers):
    test = list(permutations(numbers, len(numbers)))
    numberList = []
    for i in test:
        tempList = list(i)
        numberList.append(int(''.join(map(str, tempList))))

    numberList = sorted(numberList, reverse=True)

    answer = str(numberList[0])
    return answer


print(solution([3, 30, 34, 5, 9]))
