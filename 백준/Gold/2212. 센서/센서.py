import sys

input = sys.stdin.read().split()

N, K = int(input[0]), int(input[1])

sensor_list = list(set(map(int, input[2:N+2])))
sensor_list.sort()

diff = []
for i in range(len(sensor_list)-1):
    diff.append(sensor_list[i+1] - sensor_list[i])

diff_sorted = sorted(diff, reverse=True)
print(diff_sorted)

# 예외 처리
# 집중국이 K개 있으면 K-1개의 가장 큰거리 차이를 커팅
if K > 1:
    result = sum(diff_sorted[K-1:])
else:
    result = sum(diff)  # 집중국1개일때
print(result)

#[3, 2, 2, 1] -> [2-1:] -> 5
#[3, 3, 2, 2, 2, 2, 1, 1, 1] -> [5-1:] -> 7
