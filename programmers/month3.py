import sys
input = sys.stdin.readline
print = sys.stdout.write

#balloon = list(map(int, input().split()))

balloon = [-16,27,65,-2,58,-92,-71,-68,-61,-33]
bal1 = [0 for i in range(len(balloon))]
bal2 = [0 for i in range(len(balloon))]

min = balloon[0]

for i in range(len(balloon)):
    if balloon[i] <= min :
        bal1[balloon.index(min)] = 1
        min = balloon[i]

min = balloon[len(balloon)-1]

for i in range(len(balloon)-1 , -1 , -1):
    if balloon[i] <= min :
        bal1[balloon.index(min)] = 1
        min = balloon[i]


for i in range(len(balloon)):
    print(str(bal1[i]) + "   "  + str(bal2[i]) + "\n")