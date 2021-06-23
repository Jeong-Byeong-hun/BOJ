answer = 0

number = list(map(int, input().split(' ')))

for i in number:
    answer = answer + (i ** 2)

answer = int(answer) % 10

print(answer)
