li = []

for i in range(int(input())):
    number = int(input())
    if number == 0:
        if len(li) != 0:
            li.pop()
        else:
            continue
    else:
        li.append(number)

sum = 0

for i in li:
    sum += i

print(sum)
