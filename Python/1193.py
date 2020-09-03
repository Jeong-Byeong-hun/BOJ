
a = int(input())
i = 0

while a>0:
    a -= i
    i += 1

a = i+a - 1
answer = str(a) +'/'+str(i-a)
if i % 2 ==0 :
    answer = str(i-a) +'/'+str(a)

print(answer)