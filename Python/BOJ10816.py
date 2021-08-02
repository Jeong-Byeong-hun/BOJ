from collections import Counter

n = int(input())
aList = list(map(int, input().split(' ')))
m = int(input())
bList = list(map(int, input().split(' ')))

c = Counter(aList)

# for i in bList:
#     if i in cDict:
#         answer += str(cDict.get(i))
#     else:
#         answer += '0'
#     answer += ' '

print(' '.join(f'{c[i]}' if i in c else '0' for i in bList))
