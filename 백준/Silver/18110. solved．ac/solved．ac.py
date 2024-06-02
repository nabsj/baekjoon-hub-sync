import sys
from collections import deque

input = list(map(int, sys.stdin.read().split()))

N = input[0]
if N == 0:
    print(0)
    exit()
lst = deque(sorted(input[1:N+1]))

def round2(num):
    if num % 1 >= 0.5:
        return int((num // 1) + 1)
    else:
        return int((num // 1))

#절사평균 제외 개수
M = round2(N * 0.15)

for _ in range(M):
    lst.popleft()
    lst.pop()
print(round2(sum(lst)/len(lst)))