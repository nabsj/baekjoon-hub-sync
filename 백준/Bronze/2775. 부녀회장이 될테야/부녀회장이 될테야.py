import sys

input = list(map(int, sys.stdin.read().split()))

T = input[0]
lst = []
for i in range(T):
    lst.append([input[i*2 + 1], input[i*2 + 2]])

for i in lst:
    k = i[0]
    n = i[1]

    dp_start = []
    for o in range(1, n+1):
        dp_start.append(o)

    dp = []
    dp.append(dp_start)

    
    for j in range(1,k+1):
        tmp = 0
        dp_tmp = []
        for p in range(0,n):
            tmp += dp[j-1][p]
            dp_tmp.append(tmp)
        
        dp.append(dp_tmp)

    print(dp[k][n-1])