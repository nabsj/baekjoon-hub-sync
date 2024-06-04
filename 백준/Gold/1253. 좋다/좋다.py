N = int(input())
lst = list(map(int, input().split()))

count = 0
for i in range(len(lst)):
    #print(lst[i])
    tmp = lst[:i] + lst[i+1:]
    tmp.sort()
    #print(tmp)

    target = lst[i]
    start, end = 0, len(tmp)-1
    while start < end:
        tot = tmp[start] + tmp[end]
        #print(tmp[start], tmp[end])
        #print('target는: ', target, ' 합은 : ', tot)
        if target > tot:
            start += 1
            #print('start 1증가')
        elif target < tot:
            end -= 1
            #print('end 1하락')
        else:
            count += 1
            #print(count, '카운트 1 증가')
            break

        
    #print('---------')
print(count)
