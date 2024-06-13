import sys
sys.setrecursionlimit(10**6)

N, P, Q, X, Y = map(int, sys.stdin.readline().split())

memo = {}

def func1(num):
    if num <= 0:
        return 1
    if num in memo:
        return memo[num]
    memo[num] = func1((num // P) - X) + func1((num // Q) - Y)
    return memo[num]
print(func1(N))