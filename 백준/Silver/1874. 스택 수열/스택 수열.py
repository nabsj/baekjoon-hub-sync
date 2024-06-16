import sys

input = list(map(int, sys.stdin.read().split()))

N = input[0]

lst = input[1:N+1]

stack = []
o_idx = 0

res = []
element = 1
while element <= N + 1:
    if o_idx == N:
        break
    if len(stack) != 0 and lst[o_idx] == stack[-1]:
        stack.pop()
        res.append('-')
        o_idx += 1
    else:
        stack.append(element)
        res.append('+')
        element += 1

if len(stack) != 0:
    print('NO')
else:
    for j in res:
        print(j)