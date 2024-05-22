input = list(map(int, input().split()))

lst = [True] * (input[1] + 1)
lst[0], lst[1] = False, False

for i in range(2, int(input[1]**0.5) + 1):
    if lst[i]:
        for o in range(i**2, input[1] + 1, i):
            lst[o] = False

for q in range(input[0], input[1] + 1):
    if lst[q]:
        print(q)
