import sys

input = sys.stdin.read().split()

N = int(input[0])

index =1
for _ in range(N):
    print(input[index][0] + input[index][-1])
    index += 1