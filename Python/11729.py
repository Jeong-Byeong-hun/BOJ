def hanoi(n,f,s,t):
    if n == 1:
       print(f , t)
    else:
        hanoi(n-1,f,t,s)
        hanoi(1,f,s,t)
        hanoi(n-1,s,f,t)
