N = int(input())

if N == 1:
    print(1)
else:
    empty = [1, 2]
    for i in range(3,N+1):
        empty.append(empty[i-2] + empty[i-3])
    print(empty[-1] % 10007)