import sys
import math

input = sys.stdin.readline

idx = 1
while True:
    lst = list(map(int, input().split()))

    if sum(lst) == 0:
        break
    
    print(f'Triangle #{idx}')
    if lst[0] == -1:
        tmp = (lst[2]**2) - (lst[1]**2)
        if tmp <= 0:
            print('Impossible.')
        else:
            print("a = {:.3f}".format(math.sqrt(tmp)))
    elif lst[1] == -1:
        tmp = (lst[2]**2) - (lst[0]**2)
        if tmp <= 0:
            print('Impossible.')
        else:
            print("b = {:.3f}".format(math.sqrt(tmp)))
    elif lst[2] == -1:
        tmp = (lst[0]**2) + (lst[1]**2)
        print("c = {:.3f}".format(math.sqrt(tmp)))
    
    idx += 1
    print()
