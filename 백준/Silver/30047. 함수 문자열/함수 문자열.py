input_string = input()

stack = []
error_flag = False

i = len(input_string) - 1
while i >= 0:
    if input_string[i] == 'x':
        stack.append(0)
    elif input_string[i] == 'g':
        if not stack:
            error_flag = True
            print(-1)
            break
        stack[-1] += 1
    elif input_string[i] == 'f':
        if len(stack) < 2:
            error_flag = True
            print(-1)
            break
        a = stack.pop()
        b = stack.pop()
        stack.append(min(a, b))
    else:
        error_flag = True
        print(-1)
        break
    i -= 1

if not error_flag:
    if len(stack) == 1:
        print(stack[0])
    else:
        print(-1)
