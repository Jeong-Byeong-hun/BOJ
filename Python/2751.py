import sys

li = []
for i in range(int(input())):
    li.append(int(sys.stdin.readline()))

for i in sorted(li):
    sys.stdout.write(str(i) + '\n')

