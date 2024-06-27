import sys

input = sys.stdin.readline

N = int(input())

lst = []
V_lst = [i for i in range(1, N+1)]

min_cost = 0

for i in range(1, N + 1):
    tmp = input().split()
    for j in range(i+1, N+1):
        if int(tmp[j-1]) > 0:
            lst.append([i, j, int(tmp[j-1])])
        else:
            min_cost += (-int(tmp[j-1]))
            lst.append([i, j, 0])



edges = sorted(lst, key=lambda x: x[2])

total_cost = 0

root = dict()
for i in range(1, N+1):
    root[i] = i

def find(x):
    if root[x] == x:
        return x
    else:
        root[x] = find(root[x])
        return root[x]

def union(x, y):
    x = find(x)
    y = find(y)
    root[y] = x

res = []

for edge in edges:
    '''사이클이 만들어지는 edge라면 pass.'''    
    if find(edge[0]) == find(edge[1]):        
        continue    
    else:
        total_cost += edge[2]
        if edge[2] != 0:
            res.append([edge[0], edge[1]])
        union(edge[0], edge[1])

print(*(total_cost + min_cost, len(res)))
for p in res:
    print(*p)