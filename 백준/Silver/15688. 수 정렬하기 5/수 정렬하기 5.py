import sys

input = list(map(int, sys.stdin.read().split()))

lst = input[1:]

for i in sorted(lst):
    print(i)