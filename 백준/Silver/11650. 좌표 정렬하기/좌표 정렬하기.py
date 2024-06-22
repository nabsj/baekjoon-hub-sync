import sys

input = list(map(int, sys.stdin.read().split()))

N = input[0]

position = []

for i in range(1, 2*N + 1, 2):
    position.append((input[i], input[i+1]))

for j in sorted(position, key=lambda x: (x[0], x[1])):
    print(*j)