import sys

input = sys.stdin.read().split()

N = int(input[0])
K = int(input[1])
list = list(map(int, input[2:N+2]))

diff = []

for i in range(N-1):
    diff.append(int(list[i+1]) - int(list[i]))

#print(sorted(diff))
print(sum(sorted(diff)[:(N-K)])) # K개는 기준으로 사용, N-K는 차이값을 나타내는거임
