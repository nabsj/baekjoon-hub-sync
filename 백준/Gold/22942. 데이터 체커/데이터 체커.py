import sys

num = int(sys.stdin.readline().strip())

circle = []

for i in range(num):
    x, r = map(int, sys.stdin.readline().split())
    start = x - r
    end = x + r
    circle.append((start, end, x))

circle.sort()
#print(circle)
# (5) 1~9
# (3) 2~4
# (6) 5~7
# (13) 10~16

#print(circle)

# 모든 원이 조건에 만족하는지 확인
valid = True
for i in range(num-1):
    #for j in range(i + 1, num):
    # 중심 사이의 거리
    distance = abs(circle[i][2] - circle[i+1][2])
    # 반지름 합과 차
    radius_sum = (circle[i][2] - circle[i][0]) + (circle[i+1][2] - circle[i+1][0])
    radius_diff = abs((circle[i][2] - circle[i][0]) - (circle[i+1][2] - circle[i+1][0]))
    
    # 서로 만나지 않는 조건
    if not (distance > radius_sum or distance < radius_diff):
        valid = False
        break

result = "YES" if valid else "NO"
print(result)