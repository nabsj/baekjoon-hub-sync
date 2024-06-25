import sys
input = sys.stdin.readline

N, M = map(int, input().split())

known_lst = list(map(int, input().split()))
known_p_num = known_lst[0]
if known_p_num == 0:
    known_p = []
else:
    known_p = known_lst[1:]

parties = []
for _ in range(M):
    party = list(map(int, input().split()))
    parties.append(party[1:])

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    rootX = find(parent, x)
    rootY = find(parent, y)
    
    if rootX != rootY:
        if rank[rootX] > rank[rootY]:
            parent[rootY] = rootX
        elif rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        else:
            parent[rootY] = rootX
            rank[rootX] += 1

# Union-Find 구조 초기화
parent = list(range(N + 1))
rank = [0] * (N + 1)

# 진실을 아는 사람들을 하나의 집합으로 합침
for i in range(1, len(known_p)):
    union(parent, rank, known_p[0], known_p[i])

# 각 파티에 참석한 사람들을 같은 집합으로 묶음
for party in parties:
    for i in range(1, len(party)):
        union(parent, rank, party[0], party[i])

# 과장된 이야기를 할 수 있는 파티의 수를 계산
can_lie = 0
truth_root = {find(parent, p) for p in known_p}

for party in parties:
    if all(find(parent, p) not in truth_root for p in party):
        can_lie += 1

print(can_lie)