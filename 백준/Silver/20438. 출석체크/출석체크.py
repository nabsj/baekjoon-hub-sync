import sys

input = sys.stdin.read().split()
N, K, Q, M = int(input[0]), int(input[1]), int(input[2]), int(input[3])

idx = 4
sleep_stu = list(map(int, input[idx:idx+K])) #졸고있는 학생들
idx += K
code_stu = list(map(int, input[idx:idx+Q])) #출석코드를 받는애들
idx += Q

#print(sleep_stu)
#print(code_stu)

# 졸고 있는 학생을 True로 마킹하는 배열
sleeping = [False] * (N + 3)
for i in sleep_stu:
    sleeping[i] = True

attended = [False] * (N + 3) # 출석 했는지 확인용

for o in code_stu:
    if not sleeping[o]:  # 안졸고있는 학생만 처리
        for num in range(o, N + 3, o): # 부여받은 배수로 순회
            if not sleeping[num]: #졸지도 않고, 코드도 받아야함
                attended[num] = True

# prefix sum을 구해서 출석하지 않은 학생 수를 계산
non_attended_sum = [0] * (N + 3)
for i in range(3, N + 3): #3번부터 N+2번까지
    non_attended_sum[i] = non_attended_sum[i-1] + (0 if attended[i] else 1)

result = []
for _ in range(M):
    S = int(input[idx])
    idx += 1
    E = int(input[idx])
    idx += 1 
    if S < 3 or E > N + 2:
        result.append('0')
    else:
        result.append(str(non_attended_sum[E] - non_attended_sum[S-1]))

# 결과 출력
print("\n".join(result))