import sys
from collections import Counter

input = sys.stdin.read
data = input().split()

N = int(data[0])
numbers = list(map(int, data[1:]))

# 산술평균 계산
mean = round(sum(numbers) / N)

# 중앙값 계산
numbers.sort()
median = numbers[N // 2]

# 최빈값 계산
counter = Counter(numbers)
most_common = counter.most_common()
max_freq = most_common[0][1]

modes = [num for num, freq in most_common if freq == max_freq]
modes.sort()
if len(modes) > 1:
    mode = modes[1]  # 두 번째로 작은 최빈값
else:
    mode = modes[0]  # 최빈값이 하나뿐일 경우 그 값

# 범위 계산
range_value = numbers[-1] - numbers[0]

# 결과 출력
print(mean)
print(median)
print(mode)
print(range_value)