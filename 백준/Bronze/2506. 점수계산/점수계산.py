import sys

input = sys.stdin.readline

N = int(input())

res = list(map(int, input().split()))

sum = 0
tmp = 0
for i in res:
    if i == 1:
        tmp += 1
        sum += tmp
    else:
        tmp = 0
    
print(sum)