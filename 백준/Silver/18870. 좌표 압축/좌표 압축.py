import sys

input = sys.stdin.read().split()

N = int(input[0])
lst = list(map(int, input[1:N+1]))
#입력끝

lst2 = list(set(lst))
lst2.sort()

dict = {}
for i in range(len(lst2)):
    dict[lst2[i]] = i

results = []
for o in lst:
    results.append(dict[o])

print(*results)