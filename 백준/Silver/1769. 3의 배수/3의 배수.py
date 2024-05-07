def is_multiple_of_three(num):
    count = 0
    while len(num) > 1:
        count += 1
        num = str(sum(int(digit) for digit in num))
    
    # 마지막 한 자리 수에 대한 처리
    last_digit = int(num)
    if last_digit in [3, 6, 9]:
        return (count, "YES")
    else:
        return (count, "NO")

# 입력 받기
import sys
input = sys.stdin.read().strip()
transform_count, result = is_multiple_of_three(input)

print(transform_count)
print(result)
