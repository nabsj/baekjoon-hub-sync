import sys
from collections import deque

input = sys.stdin.read().split('\n')
N = int(input[0])
queue = deque()

for i in range(1, N+1):
    command = input[i].split()

    if command[0] == 'push':
        queue.append(command[1])

    elif command[0] == 'pop':
        if not queue:
            print('-1')
        else:
            print(queue.popleft())

    elif command[0] == 'size':
        print(len(queue))

    elif command[0] == 'empty':
        if not queue:
            print('1')
        else:
            print('0')

    elif command[0] == 'front':
        if not queue:
            print('-1')
        else:
            print(queue[0])

    elif command[0] == 'back':
        if not queue:
            print('-1')
        else:
            print(queue[-1])
