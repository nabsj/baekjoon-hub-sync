MOD = 1000000007

def cow_hopscotch(R, C, K, grid):
    dp = [[0] * C for _ in range(R)]
    dp[0][0] = 1  # 시작점 초기화

    # DP 배열 채우기
    for r in range(R):
        for c in range(C):
            if dp[r][c] > 0:  # 현재 셀에서 경로가 있는 경우만 처리
                for nr in range(r + 1, R):
                    for nc in range(c + 1, C):
                        if grid[nr][nc] != grid[r][c]:
                            dp[nr][nc] = (dp[nr][nc] + dp[r][c]) % MOD
    
    return dp[R-1][C-1]

# 입력 받기
import sys
input = sys.stdin.read
data = input().split()

R = int(data[0])
C = int(data[1])
K = int(data[2])

grid = []
index = 3
for i in range(R):
    row = []
    for j in range(C):
        row.append(int(data[index]))
        index += 1
    grid.append(row)

# 결과 출력
result = cow_hopscotch(R, C, K, grid)
print(result)
