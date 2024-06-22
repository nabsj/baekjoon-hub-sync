import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

deque = deque()

for _ in range(N):
    
    command = input().split()
    if command[0] == 'push':
        deque.append(int(command[1]))

    elif command[0] == 'pop':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.popleft())


    elif command[0] == 'size':
        print(len(deque))

    elif command[0] == 'empty':
        if len(deque) == 0:
            print(1)
        else:
            print(0)

    elif command[0] == 'front':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])

    elif command[0] == 'back':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[-1])