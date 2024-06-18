import sys

input = sys.stdin.read().split()
res = []

for idx in input:
    i = float(idx)

    if i == 0.0:
        break
    
    total = 0.0
    n = 2
    while total < i:
        total += 1.0 / n
        n += 1
    
    res.append(f"{n - 2} card(s)")

print('\n'.join(res))