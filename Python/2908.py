test1, test2 = input().split()

test1 = test1[::-1]
test2 = test2[::-1]

test1 = int(test1)
test2 = int(test2)

if test1 > test2:
    print(test1)
else:
    print(test2)


