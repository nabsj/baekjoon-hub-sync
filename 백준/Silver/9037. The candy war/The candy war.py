import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    lst = list(map(int, input().split()))

    for i in range(N):
        if lst[i] % 2 == 1:
            lst[i] += 1

    count = 0
    while len(set(lst)) != 1:
        count += 1
        tmp = [0] * N
        
        for i in range(N):
            give = lst[i] // 2
            tmp[i] -= give
            tmp[(i + 1) % N] += give
        
        for i in range(N):
            lst[i] += tmp[i]
            if lst[i] % 2 == 1:
                lst[i] += 1
    
    print(count)



        
            