import sys

input = sys.stdin.read
data = input().split()
n = int(data[0])
sizes = list(map(int, data[1:]))

snowmen = []

for i in range(n):
    for j in range(i+1, n):
        snowmen.append((sizes[i] + sizes[j], i, j))

snowmen.sort()

min_diff = float('inf')  # 차이의 최소값을 저장할 변수, 초기값은 무한대

for k in range(1, len(snowmen)):
    if (snowmen[k-1][1] != snowmen[k][1] and snowmen[k-1][1] != snowmen[k][2] and
        snowmen[k-1][2] != snowmen[k][1] and snowmen[k-1][2] != snowmen[k][2]):
        diff = abs(snowmen[k][0] - snowmen[k-1][0])
        if diff < min_diff:
            min_diff = diff

print(min_diff)