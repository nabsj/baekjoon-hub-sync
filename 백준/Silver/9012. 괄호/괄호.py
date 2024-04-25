import sys
input = sys.stdin.read().split()
N = int(input[0])

def distingush_VPS(string):
    stack = 0
    for o in string:
        if o == '(':
            stack += 1
        elif o == ')':
            if stack <= 0:
                return print("NO")
            stack -= 1

    if stack == 0:
        return print("YES")
    else:
        return print("NO")

for i in range(N):
    distingush_VPS(input[i+1])