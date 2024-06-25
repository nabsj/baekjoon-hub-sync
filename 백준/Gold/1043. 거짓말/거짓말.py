import sys
input = sys.stdin.readline

N, M = map(int, input().split())

known_lst = list(map(int, input().split()))
known_p_num = known_lst[0]
if known_p_num == 0:
    known_p = set()
else:
    known_p = set(known_lst[1:])

parties = []
for _ in range(M):
    parties.append(list(map(int, input().split()))[1:])

known_people = known_p.copy()


for _ in range(M):
    for party in parties:
        if known_people & set(party):
            known_people.update(party)
            

count = 0
for party in parties:
    if not (known_people & set(party)):
        count += 1

print(count)
