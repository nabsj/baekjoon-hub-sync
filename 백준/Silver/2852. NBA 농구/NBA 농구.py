import sys

def time_diff(pri_time, next_time):
    pri_min, pri_sec = map(int, pri_time.split(':'))
    next_min, next_sec = map(int, next_time.split(':'))

    pri_seconds = pri_min * 60 + pri_sec
    next_seconds = next_min * 60 + next_sec

    diff_seconds = next_seconds - pri_seconds

    return diff_seconds

N = int(sys.stdin.readline())

events = [['3', '00:00']]  # 경기 시작을 3으로 설정
for i in range(N):
    tmp = sys.stdin.readline().split()
    events.append(tmp)

events.append(['3', '48:00'])  # 경기 종료를 추가

t1_time = 0
t2_time = 0
last_time = "00:00"
leading_team = None
team1_score = 0
team2_score = 0

for i in range(1, len(events)):
    cur_team = events[i][0]
    cur_time = events[i][1]
    
    if leading_team == '1':
        t1_time += time_diff(last_time, cur_time)
    elif leading_team == '2':
        t2_time += time_diff(last_time, cur_time)
    
    if cur_team == '1':
        team1_score += 1
    elif cur_team == '2':
        team2_score += 1
    
    if team1_score > team2_score:
        leading_team = '1'
    elif team2_score > team1_score:
        leading_team = '2'
    else:
        leading_team = None  # 동점인 경우 리드 팀 없음
    
    last_time = cur_time

# 결과 시간 변환 및 출력
t1_min, t1_sec = divmod(t1_time, 60)
t2_min, t2_sec = divmod(t2_time, 60)

print(f"{t1_min:02}:{t1_sec:02}")
print(f"{t2_min:02}:{t2_sec:02}")
