import sys

input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
    lst.append(int(input()))

def two_value(num1, num2):
    return True if num1 > num2 else False

count = 0

while True:
    chk = [0 for _ in range(N-1)]
    for i in range(len(lst) - 1):
        if lst[i] >= lst[i + 1]:
            minus = abs(lst[i] - lst[i + 1]) + 1
            lst[i] -= minus
            count += minus
        else:
            chk[i] += 1
    
    if sum(chk) == (N-1):
        break
        
print(count)