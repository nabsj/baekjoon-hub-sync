import sys
input = sys.stdin.read().split()

N = int(input[0])

start = []
end = []

index = 1
for _ in range(N):
    Si = int(input[index])
    Ti = int(input[index+1])
    start.append(Si)
    end.append(Ti)
    index += 2

start.sort()
end.sort()

class_num = 0
start_pointer = 0
end_pointer = 0

while start_pointer < N:
    if start[start_pointer] < end[end_pointer]:
        # 가장 일찍 끝나는 시간보다 작으면 num + 1
        class_num += 1
    else:
        #print(start[start_pointer], end[end_pointer])
        end_pointer += 1
    start_pointer += 1

print(class_num)