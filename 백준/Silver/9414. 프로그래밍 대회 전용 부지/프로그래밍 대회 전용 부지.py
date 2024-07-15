import sys

input = list(map(int, sys.stdin.read().split()))

T = int(input[0])

input = input[1:]

lst = []

tmp = []
for i in input:
    if i == 0:
        lst.append(tmp)
        tmp = []
    else:
        tmp.append(i)



for p in range(T):
    tmp2 = sorted(lst[p], reverse=True)
    tot = 0
    idx = 1
    chk = None
    for j in tmp2:
        tot += 2 * (j**idx)
        idx += 1
        if tot >= 5 * (10**6):
            chk = True
            break
    
    if chk == True:
        print('Too expensive')
    else:
        print(tot)