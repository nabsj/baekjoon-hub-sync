import sys

input = sys.stdin.read
data = input().split()
K = int(data[0])
node_list = list(map(int, data[1:]))

def inorder_index(node_index, current_dep, max_dep): #중위순회
    if current_dep > max_dep:
        return []
    mid = (node_index * 2 + 1)
    left = inorder_index(node_index * 2 + 1, current_dep + 1, max_dep)
    current = [node_index]
    right = inorder_index(node_index * 2 + 2, current_dep + 1, max_dep)
    return left + current + right

res = inorder_index(0, 0, K-1)

tree = [0] * (2**K - 1)
for i, index in enumerate(res):
    tree[index] = node_list[i]

# BFS순서로 바꿈

for dep in range(K):
    start = 2**dep - 1
    end = 2**(dep + 1) - 1
    print(' '.join(map(str, tree[start:end])))



'''
            0
        1         2
      3  4     5     6
    7 8 9 10 11 12 13 14

0 1 3 7 -> 2p + 1

0 2 6 14 -> 2p + 2
'''
    