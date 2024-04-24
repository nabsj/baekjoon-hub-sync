import sys

def min_square_sum(n):
    dp = [float('inf')] * (n + 1)
    dp[0] = 0  # 초기값 0
    
    # 모든 가능한 제곱수를 계산
    squares = [i * i for i in range(1, int(n**(1/2)) + 1)]
    
    for i in range(1, n + 1):
        for square in squares:
            if square > i:
                break
            dp[i] = min(dp[i], dp[i - square] + 1)
    
    return dp[n]

n = int(sys.stdin.read().strip())
print(min_square_sum(n))