text = input()
alpa = []

for i in range(26):
    alpa.append(-1)

for index, value in enumerate(text):
    ask = 97
    for i in range(26):
        if chr(ask) in value:
            if alpa[ask - 97] == -1:
                alpa[ask - 97] = index
        ask += 1


for i in alpa:
    print(i,end=" ")