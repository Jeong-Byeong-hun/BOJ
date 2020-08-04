test = int(input())

for i in range(test):
    temp_num, temp_text = input().split()
    answer = ""
    for j in temp_text:
        answer += j * int(temp_num)

    print(answer)