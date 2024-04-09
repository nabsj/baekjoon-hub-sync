import sys

num = int(sys.stdin.readline().strip())

stack = []
output = []

for _ in range(num):
    e = sys.stdin.readline().strip().split()

    if e[0] == "push":
        stack.append(e[1])

    elif e[0] == "pop":
        if not stack:
            output.append('-1')
        else:
            output.append(stack.pop())
    
    elif e[0] == "size":
        output.append(str(len(stack)))
    
    elif e[0] == "empty":
        output.append('1' if not stack else '0')

    elif e[0] == "top":
        output.append('-1' if not stack else stack[-1])

print('\n'.join(output))
