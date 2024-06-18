import sys

input = sys.stdin.read().strip().split('\n')

for i in input:
    numbers = list(map(int, i.split()))
    n = numbers[0]
    lst = numbers[1:]
    
    if n == 1:
        print("Jolly")
        continue
    
    diffs = set()
    jolly = True
    for i in range(n-1):
        diff = abs(lst[i] - lst[i+1])
        if diff < 1 or diff >= n or diff in diffs:
            jolly = False
            break
        diffs.add(diff)
    
    if jolly and len(diffs) == n - 1:
        print("Jolly")
    else:
        print("Not jolly")