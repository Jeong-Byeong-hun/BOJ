def solution(n):
    answer = 0

    return answer


def three(n):
    q, r = divmod(n, 3)
    if q == 0:
        return r
    else:
        return three(q) + r


def convert(n):
    Text = "012"
    q, r = divmod(n, 3)

    if q == 0:
        return Text[r]
    else:
        return convert(q) + Text[r]

a = convert(45);

answer = 0
for i in range(len(a)):
    answer += int(a[i]) * (3 ** i)

print(answer)


