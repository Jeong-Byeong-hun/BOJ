#Knapsack Problem
#배낭의 한도 = DP
#무게 = W
#가치 = V
#수 = N

import sys, math
input = sys.stdin.readline
print = sys.stdout.write

n, k = map(int, input().split(' '))

w = []
v = []
dp = [[0 for i in range(k+1)]for i in range(n+1)]


for i in range(n):
    x ,y = map(int, input().split(' '))
    w.append(x)
    v.append(y)


for i in range(n+1):
    for j in range(k+1):
        if i ==0 or j ==0 :
            dp[i][j] = 0
        elif w[i-1] <= j:
            dp[i][j] = max(v[i-1] + dp[i-1][j-w[i-1]], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

print(str(dp[n][k]))