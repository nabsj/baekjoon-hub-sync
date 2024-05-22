import sys

input = sys.stdin.read().split()

N, X = int(input[0]), int(input[1])
lst = list(map(int, input[2:N+2]))

prefix_sum = [0] * (N + 1)
for i in range(1, N + 1):
    prefix_sum[i] = prefix_sum[i-1] + lst[i-1]

max_sum = 0
count = 0

for i in range(X, N + 1):
    value = prefix_sum[i] - prefix_sum[i - X]
    if value > max_sum:
        max_sum = value
        count = 1
    elif value == max_sum:
        count += 1
        
if max_sum == 0:
    print('SAD')
else:
    print(max_sum)
    print(count)
