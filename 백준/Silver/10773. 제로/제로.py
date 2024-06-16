import sys
from collections import deque

input = sys.stdin.readline

K = int(input())

deque = deque()

for _ in range(K):
    num = int(input())
    deque.append(num)
    if num == 0:
        deque.pop()
        deque.pop()

print(sum(deque))