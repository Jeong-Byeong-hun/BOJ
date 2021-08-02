def solution(a, b):
    answer = 0

    for i in range(len(a)):
        answer += a[i] * b[i]
    return answer

a = [1,2,3,4]
b = [-3,-1,0,2]

# print(solution(a, b))

def solution2(s):
    answer = [0,0]
    temp = 0
    strs = s
    while True:
        if s == 1:
            break
        s = zeroDel(s)
        print(s)
        temp = len(strs) - s

        answer[0] += 1
        answer[1] += temp
        s = two(temp)
        strs = s
        print(s)

    return answer

def zeroDel(s):
    s = s.replace("0","")
    return len(s)



def two(n):
  return format(n,'b')

print(solution2("110010101001"))

# print(two(6))