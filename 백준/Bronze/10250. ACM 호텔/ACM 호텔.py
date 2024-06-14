import sys

input = list(map(int, sys.stdin.read().split()))

N = input[0]

for i in range(N):
    H, W, N = input[3 * i + 1], input[3 * i + 2], input[3 * i + 3]
    floor = N % H
    room = N // H + 1
    if floor == 0:
        floor = H
        room -= 1
    print(f"{floor}{room:02d}")