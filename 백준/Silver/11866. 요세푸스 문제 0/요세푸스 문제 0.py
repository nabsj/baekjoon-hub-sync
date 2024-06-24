import sys

input = sys.stdin.readline().split()

N, K = int(input[0]), int(input[1])

lst = list(range(1, N + 1))
result = []
idx = 0 

while lst:
    idx = (idx + K - 1) % len(lst)
    result.append(lst.pop(idx))

print("<" + ", ".join(map(str, result)) + ">")
