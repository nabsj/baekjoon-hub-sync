import sys

input = list(map(int, sys.stdin.read().split()))

N = input[0]

lst = input[1:N+1]

target = input[N+1]

tmp = 0

for i in lst:
    if i == target:
        tmp += 1

print(tmp)