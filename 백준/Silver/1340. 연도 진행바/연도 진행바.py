import sys
from datetime import datetime

input = sys.stdin.readline().split()
input[1] = input[1][:-1]
#print(input)

# year input[2] => 윤년만 계산
chk = False
if int(input[2]) % 400 == 0 or (int(input[2]) % 4 == 0 and int(input[2]) % 100 != 0):
    total_minute = 366 * 24 * 60
    chk = True
else:
    total_minute = 365 * 24 * 60

# 기본 세팅 은 분으로 고정하자
# month input[0]

if chk == True:
    nor_month_lst = [('January', 31),
                    ('February', 29),
                    ('March', 31),
                    ('April', 30),
                    ('May', 31),
                    ('June', 30),
                    ('July',31),
                    ('August',31),
                    ('September',30),
                    ('October', 31),
                    ('November', 30),
                    ('December',31)]
else:
    nor_month_lst = [('January', 31),
                    ('February', 28),
                    ('March', 31),
                    ('April', 30),
                    ('May', 31),
                    ('June', 30),
                    ('July',31),
                    ('August',31),
                    ('September',30),
                    ('October', 31),
                    ('November', 30),
                    ('December',31)]

month_sum = 0
for i in nor_month_lst:
    if input[0] == i[0]:
        break
    else:
        month_sum += (i[1] * 24 * 60)

# day input[1]
day_sum = 0
day_sum += (int(input[1])-1) * 24 * 60



# time input[3]
HH, MM = input[3].split(':')
min_sum = 0
min_sum = int(HH) * 60 + int(MM)

# print(month_sum)
# print(day_sum)
# print(min_sum)

print((month_sum + day_sum + min_sum) / total_minute * 100)