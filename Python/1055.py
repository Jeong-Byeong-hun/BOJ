first_text = input()
change_text = input()
repeat = int(input())
start_range , end_range = map(int, input().split(' '))

for i in range(repeat):
    first_text = change_text.replace('$', first_text)

print(first_text[start_range-1:end_range])

#메모리 초과
