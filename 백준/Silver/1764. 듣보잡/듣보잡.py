N, M = map(int, input().split())  # 듣도 못한 사람의 수 N, 보도 못한 사람의 수 M

not_heard = {input() for _ in range(N)}

not_seen = {input() for _ in range(M)}

not_heard_seen = sorted(list(not_heard & not_seen))

print(len(not_heard_seen))
for name in not_heard_seen:
    print(name)