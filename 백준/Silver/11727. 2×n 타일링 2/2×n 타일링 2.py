N = int(input())

if N == 1:
    print(1)
elif N == 2:
    print(3)
else:
    empty = [1, 3]
    for i in range(2, N): # 3으로 했을때는 안맞음
        empty.append(empty[i-1] + 2 * empty[i-2]) 
    print(empty[-1] % 10007)


# 1 1 - 세
# 2 3 - 가가, 세세, 네모
# 3 5 - 가가세, 세가가, 세세세, 네모세, 세네모
# 4 11 - 네모네모, 네모가가, 가가네모, 네모세세, 세네모세, 세세네모, 가가가가, 가가세세, 세가가세, 세세가가, 세세세세