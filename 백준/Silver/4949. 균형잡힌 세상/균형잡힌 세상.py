import sys

input = sys.stdin.read().strip().split('\n')

for line in input:
    if line == '.':
        break
    
    stack = []
    balanced = True # 균형이 맞는지
    bracket = {')': '(', ']': '['} #괄호를 브라켓이라고한다

    for char in line:
        if char in bracket.values():
            stack.append(char)
        elif char in bracket.keys():
            if stack and stack[-1] == bracket[char]:
                stack.pop()
            else:
                balanced = False
                break

    if balanced and not stack:
        print("yes")
    else:
        print("no")