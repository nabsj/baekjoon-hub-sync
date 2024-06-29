N = int(input())

lst = list(map(int, input().split()))
lst = sorted(lst, reverse=True)

count = 0

while True:
    if sum(lst) == 0:
        print(count)
        break
    elif count > 1439:
        print(-1)
        break
    
    if len(lst) > 1:
        if lst[1] != 0:
            lst[0] -= 1
            lst[1] -= 1
            count += 1
            lst = sorted(lst, reverse=True)
        else:
            lst[0] -= 1
            count += 1
            lst = sorted(lst, reverse=True)
    else:
        lst[0] -= 1
        count += 1
        lst = sorted(lst, reverse=True)