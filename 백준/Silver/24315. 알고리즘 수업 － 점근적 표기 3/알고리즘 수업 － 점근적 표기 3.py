a1, a0 = map(int, input().split())
c1, c2 = map(int, input().split())
n0 = int(input())

check = True
for n in range(n0, 1001):
    if not (c1 * n <= a1 * n + a0 <= c2 * n):
        check = False
        break

print(1 if check else 0)
