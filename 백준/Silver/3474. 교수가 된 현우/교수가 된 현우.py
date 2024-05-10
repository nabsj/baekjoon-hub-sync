import sys

input = sys.stdin.read().split()

T = int(input[0])

res_list = []

for i in range(1, T+1):
    n = int(input[i])
    count = 0
    while n >= 5:
        n //= 5
        count += n
    res_list.append(count)

for res in res_list:
    print(res)