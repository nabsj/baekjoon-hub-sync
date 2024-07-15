def find_path(a, b):
    left_count = 0
    right_count = 0
    
    while a != 1 or b != 1:
        if a == 1:
            right_count += b - 1
            break
        if b == 1:
            left_count += a - 1
            break
        if a > b:
            moves = a // b
            left_count += moves
            a %= b
        else:  # a < b
            moves = b // a
            right_count += moves
            b %= a
    
    return left_count, right_count

# 입력 처리
a, b = map(int, input().split())

# 결과 계산
l, r = find_path(a, b)

# 결과 출력
print(l, r)


#           1, 1
#         2,1 1,2
#    3,1 2,3    3,2, 1,3
# 4,1 3,4 5,3 2,5 


# 2,1
# 3,1 2,3
# 4,1 3,4 5,3 2,5

# 1,2
# 3,2 1,3
# 5,2 3,5 4,3 1,4

