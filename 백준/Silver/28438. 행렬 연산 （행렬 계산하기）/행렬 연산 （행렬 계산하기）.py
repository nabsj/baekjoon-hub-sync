import sys
input = sys.stdin.readline

N, M, Q = map(int, input().split())

row_add = [0] * N
col_add = [0] * M

for _ in range(Q):
    query = list(map(int, input().split()))
    
    if query[0] == 1:  # 행에 더하기
        row_add[query[1] - 1] += query[2]
    else:  # 열에 더하기
        col_add[query[1] - 1] += query[2]

for i in range(N):
    row = [row_add[i] + col_add[j] for j in range(M)]
    print(*row)
