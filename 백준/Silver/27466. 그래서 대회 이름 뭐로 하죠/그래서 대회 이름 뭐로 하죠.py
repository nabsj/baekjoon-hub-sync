def func(idx, num, remove):
    if remove == N - M:
        t = 1
        for i in range(len(str) - 1, -1, -1):
            if str[i] == '!':
                continue
            if t == 1:
                if str[i] not in 'AEIOU':
                    t += 1
                else:
                    return False
            elif t <= 3:
                if str[i] == 'A':
                    t += 1
                else:
                    return False
            if t > 3:
                return True

    if num == 1:
        if str[idx] not in 'AEIOU':
            return func(idx - 1, num + 1, remove)
        else:
            str[idx] = '!'
            return func(idx - 1, num, remove + 1)
    elif num <= 3:
        if str[idx] == 'A':
            return func(idx - 1, num + 1, remove)
        else:
            str[idx] = '!'
            return func(idx - 1, num, remove + 1)
    else:
        str[idx] = '!'
        return func(idx - 1, num, remove + 1)

    return True

# 입력 처리
N, M = map(int, input().split())
str = list(input().strip())  # 문자열을 리스트로 변경

if func(len(str) - 1, 1, 0):
    print("YES")
    print(''.join([ch for ch in str if ch != '!']))
else:
    print("NO")
