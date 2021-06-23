def solution(progresses, speeds):
    answer = []

    while True:
        temp = 0

        for i in range(len(progresses)):
            progresses[i] += speeds[i]

        for i in range(len(progresses)):
            if progresses[i] >= 100:
                temp += 1
            else:
                break

        if temp > 0:
            for i in range(temp):
                if progresses[0] >= 100:
                    progresses.pop(0)
                    speeds.pop(0)

            answer.append(temp)

        if len(progresses) == 0:
            break

    return answer


def solution2(progresses, speeds):
    Q = []
    for p, s in zip(progresses, speeds):
        if len(Q) == 0 or Q[-1][0] < -((p - 100) // s):
            Q.append([-((p - 100) // s), 1])
        else:
            Q[-1][1] += 1
    return [q[1] for q in Q]


progresses1 = [95, 90, 99, 99, 80, 99]
speeds1 = [1, 1, 1, 1, 1, 1]
print(solution2(progresses1, speeds1))
