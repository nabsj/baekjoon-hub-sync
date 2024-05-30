N = int(input())

count = 0
k = 1
while k * (k - 1) // 2 < N:
    num = 2 * N - k * (k - 1)
    if num % (2 * k) == 0:
        a = num // (2 * k)
        if a > 0:
            count += 1
    k += 1

print(count)