import sys

input = list(map(int, sys.stdin.read().split()))

N = input[0]
lst = input[1:N+1]
Q = input[N+1]
Q_lst = [(input[i], input[i+1]) for i in range(N+2, (N + 2) + (2 * Q), 2)]

prefix = [0] * (N+1)

idx = 0
tmp = 0
for j in range(N):
    tmp += (1 if lst[j] - lst[j-1] < 0 else 0)
    prefix[idx+1] = tmp
    idx += 1

for o in Q_lst:
    print(prefix[o[1]] - prefix[o[0]])