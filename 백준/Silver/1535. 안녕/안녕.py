import sys

input = list(map(int, sys.stdin.read().split()))

N = input[0]
L = input[1:N+1]
J = input[N+1: 2*(N+1)]

L, J = [0] + L, [0] + J
dp = [[0 for _ in range(101)] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, 101):
        if L[i] <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-L[i]] + J[i])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[N][99])
