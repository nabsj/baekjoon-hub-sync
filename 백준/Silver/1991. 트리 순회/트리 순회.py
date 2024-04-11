import sys

num = int(sys.stdin.readline().strip())

dict = {}

#이진트리
for _ in range(num):
    input = sys.stdin.readline().strip().split()
    par = input[0]
    left_chi = input[1] if not input[1] == '.' else None
    right_chi = input[2] if not input[2] == '.' else None
    dict[par] = [left_chi, right_chi]

#print(dict)

def 전위순회(node):
    if node == None:
        return
    print(node, end='') #현재노드 출력
    전위순회(dict[node][0]) #왼쪽 방문
    전위순회(dict[node][1]) #오른쪽 방문

def 중위순회(node):
    if node == None:
        return
    중위순회(dict[node][0])
    print(node, end='')
    중위순회(dict[node][1])
    

def 후위순회(node):
    if node == None:
        return
    후위순회(dict[node][0])
    후위순회(dict[node][1])
    print(node, end='')



전위순회("A")
print()
중위순회("A")
print()
후위순회("A")