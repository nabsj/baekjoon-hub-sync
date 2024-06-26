N = int(input())
if N == 0:
    print(1)
else:
    sum = 1
    for i in range(1, N+1):
        sum *= i
    print(sum)