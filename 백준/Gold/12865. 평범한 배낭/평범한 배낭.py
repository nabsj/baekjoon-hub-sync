import sys

input = list(map(int, sys.stdin.read().split()))

N, K = input[0], input[1]  # 물품 수, 최대 버틸 수 있는 무게

weight, value = [], []
for i in range(N):
    weight.append(input[2*i + 2])
    value.append(input[2*i + 3])

weight, value = [0] + weight, [0] + value
dp = [[0 for _ in range(K+1)] for _ in range(N+1)]  # 물품 수, 최대 무게에 맞게 dp 배열 초기화

for i in range(1, N+1):
    for j in range(1, K+1):
        if weight[i] <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i]] + value[i])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N][K])


'''
     0   1   2   3   4   5   6   7   8   9  10
  +--------------------------------------------
0 |  0   0   0   0   0   0   0   0   0   0   0
1 |  0   ?   ?   ?   ?   ?   ?   ?   ?   ?   ?
2 |  0   ?   ?   ?   ?   ?   ?   ?   ?   ?   ?
3 |  0   ?   ?   ?   ?   ?   ?   ?   ?   ?   ?

'''