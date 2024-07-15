import sys

input = sys.stdin.read().split()

N = int(input[0])
lst = []

index = 1
for _ in range(N):
    X = int(input[index])
    T = int(input[index+1])
    C = int(input[index+2])
    index += 3
    lst.append((X, T, C))

cal = {}

for X, T, C in lst:
    S = X - T
    if S in cal:
        cal[S] += C
    else:
        cal[S] = C

max_value = max(cal.values())

print(max_value)
