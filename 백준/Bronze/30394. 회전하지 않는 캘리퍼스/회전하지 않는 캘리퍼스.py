import sys

input = sys.stdin.readline

N = int(input())

dots = []
for _ in range(N):
    dots.append(list(map(int, input().split())))

min_y = float('inf')
max_y = float('-inf')

for i in dots:
    x, y = i
    if y < min_y:
        min_y = y
    if y > max_y:
        max_y = y

distance = max_y - min_y

print(distance)