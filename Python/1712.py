a,b,c = input().split(' ')
cnt = 0


if int(b) >= int(c):
    print(-1)
else:
    print( int(int(a)/(int(c) - int(b)) + 1))



