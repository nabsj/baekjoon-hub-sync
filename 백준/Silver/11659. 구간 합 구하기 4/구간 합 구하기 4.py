import sys
input = sys.stdin.read().split()

N = int(input[0])
M = int(input[1])

A = [0] * N
P = [0] * (N + 1)

index = 2
for i in range(N):
    A[i] = int(input[index])
    P[i + 1] = P[i] + A[i]
    index += 1

output = []
for _ in range(M):
    i = int(input[index])
    j = int(input[index + 1])
    print(P[j] - P[i - 1])
    index += 2