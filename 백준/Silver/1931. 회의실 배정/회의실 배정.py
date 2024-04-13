n = int(input().strip())
meeting = []

for _ in range(n):
    start, end = map(int, input().split())
    meeting.append((start, end))

  
meeting.sort(key=lambda x: (x[1], x[0]))

count = 0
last_end_time = 0

# 이전의 회의 이후에 시작하는 회의 선택
for start, end in meeting:
    if start >= last_end_time:
        last_end_time = end
        count += 1

print(count)