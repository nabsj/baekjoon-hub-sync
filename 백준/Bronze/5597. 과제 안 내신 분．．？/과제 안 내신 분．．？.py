import sys

input = list(map(int, sys.stdin.read().split()))

tmp = [i for i in range(1, 31)]

for i in input:
    tmp.remove(i)

for o in tmp:
    print(o)