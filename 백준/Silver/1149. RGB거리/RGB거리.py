import sys

input = sys.stdin.read().split()

N = int(input[0])
cost = []
index = 1
for _ in range(N):
    cost.append([int(input[index]), int(input[index+1]), int(input[index+2])])
    index += 3

dp = [[0] * 3 for _ in range(N)]

dp[0][0], dp[0][1], dp[0][2] = cost[0][0], cost[0][1], cost[0][2]

for i in range(1, N):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + cost[i][2]

min_cost = min(dp[-1][0], dp[-1][1], dp[-1][2])
print(min_cost)