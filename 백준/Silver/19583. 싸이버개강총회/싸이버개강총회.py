import sys
from datetime import datetime

input = sys.stdin.read().split()
S, E, Q = input[0], input[1], input[2]

dt_S = datetime.strptime(S, "%H:%M")
dt_E = datetime.strptime(E, "%H:%M")
dt_Q = datetime.strptime(Q, "%H:%M")

att_before = set()
att_after = set()

for i in range(3, len(input), 2):
    dt_chat = datetime.strptime(input[i], "%H:%M")

    # 개총전
    if dt_chat <= dt_S:
        att_before.add(input[i+1])

    # 개총후, 스트리밍 끝까지
    if dt_E <= dt_chat <= dt_Q:
        att_after.add(input[i+1])

print(len(att_before & att_after))