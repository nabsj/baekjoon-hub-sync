import sys

input = sys.stdin.read().split()

N, M = int(input[0]), int(input[1])

print(N // M)
print(N % M)