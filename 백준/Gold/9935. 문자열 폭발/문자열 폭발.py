import sys

input = sys.stdin.read().split()
string = input[0]
bomb = input[1]
bomb_length = len(bomb)
bomb_last_char = bomb[-1]
stack = []

for char in string:
    stack.append(char)
    
    if char == bomb_last_char and len(stack) >= bomb_length:
        if stack[-bomb_length:] == list(bomb):
            del stack[-bomb_length:]

# 결과 출력
if not stack:
    print("FRULA")
else:
    print(''.join(stack))
