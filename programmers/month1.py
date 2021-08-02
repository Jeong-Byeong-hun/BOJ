numbers = [5,0,2,7]

num = numbers.sort()

def code(num):
    list = []
    for i in range(len(num)):
        for j in range(i+1, len(num)):
            number = num[i] + num[j]
            if number not in list:
                list.append(number)

    list.sort()
    print(list)

code(numbers)
