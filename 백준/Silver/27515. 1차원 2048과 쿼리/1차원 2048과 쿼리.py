import sys
import math

input = sys.stdin.readline

Q = int(input())

total_sum = 0

arr = []
arr_count = {}

for _ in range(Q):
    query = input().strip()
    op = query[0]
    num = int(query[1:])
    
    if op == '+':
        arr.append(num)
        total_sum += num
        if num in arr_count:
            arr_count[num] += 1
        else:
            arr_count[num] = 1
    elif op == '-':
        arr.remove(num)  # 이 방식 대신 arr_count를 사용하여 관리할 수도 있습니다.
        total_sum -= num
        arr_count[num] -= 1
        if arr_count[num] == 0:
            del arr_count[num]
    
    if total_sum == 0:
        print(0)
    else:
        # total_sum이 0이 아닌 경우만 log2 계산
        print(2 ** int(math.log2(total_sum)))
