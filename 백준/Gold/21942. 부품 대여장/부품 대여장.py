import sys
from datetime import datetime, timedelta

input = sys.stdin.read
data = input().splitlines()

def parse_date(date_str):
    from datetime import datetime
    return datetime.strptime(date_str, "%Y-%m-%d %H:%M")

#print(data)
def convert_minutes(time):
    days, time_part = time.split('/')
    days = int(days)
    hours, minutes = map(int, time_part.split(':'))
    total_minutes = days * 60 * 24 + hours * 60 + minutes
    return total_minutes

N, L, F = data[0].split() #정보의 개수 N, 대여기간 L, 벌금 F
N, L, F = int(N), convert_minutes(L), int(F)
#초기셋팅끝

logs =data[1:N+1]
#print(logs)

rent_times ={} #렌탈시간
fines = {} #벌금

for i in logs:
    content = i.split()
    date_time_str = ' '.join(content[:2]) # 날짜 + 시간
    part_name = content[2] #빌린 물품
    member_name = content[3] #빌린 사람

    key = (part_name, member_name)

    date_time = parse_date(date_time_str)

    if key in rent_times:
        rent_time = rent_times.pop(key) #렌트중이면 배열에서 팝
        due_time = rent_time + timedelta(minutes=L) # 반납해야하는 시각
        if date_time > due_time:
            overdue_minutes = (date_time - due_time).total_seconds() / 60
            if overdue_minutes > 0:
                fine_amount = int(overdue_minutes) * F
                if member_name in fines:
                    fines[member_name] += fine_amount
                else:
                    fines[member_name] = fine_amount
    else:
        rent_times[key] = date_time #렌트시작이면 기입

if fines:
    sorted_fines = sorted(fines.items())
    for member_name, fine_amount in sorted_fines:
        print(member_name, fine_amount)
else:
    print(-1)