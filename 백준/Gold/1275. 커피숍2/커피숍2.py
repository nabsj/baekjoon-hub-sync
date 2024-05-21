import sys

input = list(map(int, sys.stdin.read().split()))

N, Q = input[0], input[1]
base_list = input[2:N+2]
tree = [0] * (4 * N)

def build(data, node, start, end):
    if start == end:
        tree[node] = data[start]
    else:
        mid = (start + end) // 2
        build(data, 2 * node + 1, start, mid)
        build(data, 2 * node + 2, mid + 1, end)
        tree[node] = tree[2 * node + 1] + tree[2 * node + 2]

def query(left, right, node, start, end):
    if right < start or end < left:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    left_sum = query(left, right, 2 * node + 1, start, mid)
    right_sum = query(left, right, 2 * node + 2, mid + 1, end)
    return left_sum + right_sum

def update(idx, value, node, start, end):
    if start == end:
        tree[node] = value
    else:
        mid = (start + end) // 2
        if start <= idx <= mid:
            update(idx, value, 2 * node + 1, start, mid)
        else:
            update(idx, value, 2 * node + 2, mid + 1, end)
        tree[node] = tree[2 * node + 1] + tree[2 * node + 2]

build(base_list, 0, 0, N - 1)
#print(tree)

idx = N + 2
results = []
for _ in range(Q):
    x, y = input[idx: idx+2]
    if x > y:
        x, y = y, x
    
    a, b = input[idx+2: idx+4]

    print(query(x-1, y-1, 0, 0, N-1))
    update(a-1, b, 0, 0, N-1)
    idx += 4
