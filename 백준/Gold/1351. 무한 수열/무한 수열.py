import sys

N, P, Q = map(int, sys.stdin.readline().split())

memo = {}

def func1(num):
    if num == 0:
        return 1
    if num in memo:
        return memo[num]
    memo[num] = func1(num // P) + func1(num // Q)
    return memo[num]
print(func1(N))