import sys

input = list(map(int, sys.stdin.read().split()))

N, M = input[0], input[1]

A, B = [], []

idx = 2
for _ in range(M):
    tmp = []
    for _ in range(N):
        tmp.append(input[idx])
        idx += 1
    A.append(tmp)

for _ in range(M):
    tmp = []
    for _ in range(N):
        tmp.append(input[idx])
        idx += 1
    B.append(tmp)

def sumMatrix(A,B):
    answer = []
 
    for i in range(len(A)):
        tmp=[]
        for j in range(len(A[i])):
            tmp.append(A[i][j]+B[i][j])
        
        answer.append(tmp)
     
    return answer

res = sumMatrix(A,B)

for o in res:
    print(*o)