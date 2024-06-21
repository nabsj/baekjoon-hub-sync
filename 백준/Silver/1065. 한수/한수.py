def is_hansu(number):
    num_str = str(number)
    if len(num_str) <= 2:
        return True
    else:
        diff = int(num_str[1]) - int(num_str[0])
        for i in range(1, len(num_str) - 1):
            if (int(num_str[i + 1]) - int(num_str[i])) != diff:
                return False
        return True

def count_hansu(N):
    count = 0
    for i in range(1, N + 1):
        if is_hansu(i):
            count += 1
    return count

# 입력값 처리
N = int(input())

# 결과 출력
print(count_hansu(N))
