import sys
input = sys.stdin.read().split()

N = int(input[0])  # 문제 수
M = int(input[1])  # 학생 수
idx = 2

can_solve = [0] * M

for i in range(M):
    O = int(input[idx])
    idx += 1
    for _ in range(O):
        P = int(input[idx]) - 1
        can_solve[i] |= (1 << P)
        idx += 1

all_problems = (1 << N) - 1
min_team_size = float('inf')

for mask in range(1, 1 << M):
    solved = 0
    team_size = 0
    
    for i in range(M):
        if mask & (1 << i):
            solved |= can_solve[i]
            team_size += 1
    
    if solved == all_problems:
        min_team_size = min(min_team_size, team_size)

if min_team_size == float('inf'):
    print(-1)
else:
    print(min_team_size)