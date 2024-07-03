# 7일때 [+,+,+,*,*,*]
# 5일때 [+,+,+,*]

import itertools
import sys

input = sys.stdin.read().split()
N = int(input[0])
lst = list(map(int, input[1:]))

elements = ['+', '+', '+']
for _ in range(N-4):
    elements.append('*')

permutations = set(itertools.permutations(elements))

tot = 0

for perm in permutations:
    evaluate = str(lst[0])
    perm = list(perm)
    for i in range(0, N):
        if i != N-1:
            evaluate += perm[i]
            evaluate += str(lst[i+1])
    tmp = eval(evaluate)
    if tot < tmp:
        tot = tmp

print(tot)
        