import sys
num = int(sys.stdin.readline().strip())

height = list(map(int, sys.stdin.readline().split()))
res = [0]*num
stack = []

for i in range(num-1, -1, -1):  # 역순
    while stack and height[i] > stack[-1][0]: 
        #스택에 존재, 스택의마지막보다 작을때까지
        _, index = stack.pop() #(높이, 순서) 순
        res[index] = i + 1
    stack.append((height[i], i))

print(*res)