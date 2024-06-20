import sys
from itertools import combinations

input = list(map(int, sys.stdin.read().split()))

N = input[0]
train_lst = input[1:N+1]
numerous = input[N+1]

prefix = [0] * (N+1)

for i in range(0, N):
    prefix[i+1] = prefix[i] + train_lst[i]

dp = [[0] * (N + 1) for _ in range(4)] #3개 기차

for j in range(1, 4):
    for i in range(j * numerous, N + 1):
        not_include = dp[j][i - 1]
        include = dp[j-1][i-numerous]+ (prefix[i] - prefix[i-numerous])
        dp[j][i] = max(not_include, include )
        
print(dp[3][N])