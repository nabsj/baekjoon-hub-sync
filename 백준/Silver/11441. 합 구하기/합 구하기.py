import sys

input = list(map(int, sys.stdin.read().split()))

N = input[0]
lst = input[1:N+1]
M = input[N+1]
queries = input[N+2:]

prefix = [0] * (N + 1)
for i in range(1, N + 1):
    prefix[i] = prefix[i - 1] + lst[i - 1]

output = []
for i in range(0, 2 * M, 2):
    l = queries[i] - 1
    r = queries[i + 1] - 1
    if l == 0:
        print(prefix[r + 1])
    else:
        print(prefix[r + 1] - prefix[l])

