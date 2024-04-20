import sys
from bisect import bisect_left, bisect_right, insort_left

data = sys.stdin.read().splitlines()

N = int(data[0])
problem_by_group = {}
all_problems = []

for i in range(1, N+1):
    P, L, G = map(int, data[i].split())
    if G not in problem_by_group:
        problem_by_group[G] = []
    # (난이도, 문제번호) 쌍으로 관리
    insort_left(problem_by_group[G], (L, P))
    insort_left(all_problems, (L, P))

M = int(data[N+1])
commands = data[N+2:N+2+M]

results = []

def remove_problem(problems, P):
    index = bisect_left(problems, (0, P))
    while index < len(problems) and problems[index][1] != P:
        index += 1
    if index < len(problems) and problems[index][1] == P:
        problems.pop(index)

for command in commands:
    parts = command.split()
    cmd = parts[0]
    if cmd == "add":
        P, L, G = map(int, parts[1:])
        if G not in problem_by_group:
            problem_by_group[G] = []
        insort_left(problem_by_group[G], (L, P))
        insort_left(all_problems, (L, P))
    elif cmd == "solved":
        P = int(parts[1])
        for G, problems in problem_by_group.items():
            remove_problem(problems, P)
        remove_problem(all_problems, P)
    elif cmd == "recommend":
        G, x = int(parts[1]), int(parts[2])
        if x == 1:
            results.append(str(max(problem_by_group[G])[1]))
        elif x == -1:
            results.append(str(min(problem_by_group[G])[1]))
    elif cmd == "recommend2":
        x = int(parts[1])
        if x == 1:
            results.append(str(max(all_problems)[1]))
        elif x == -1:
            results.append(str(min(all_problems)[1]))
    elif cmd == "recommend3":
        x, L = int(parts[1]), int(parts[2])
        if x == 1:
            pos = bisect_left(all_problems, (L, -float('inf')))
            if pos < len(all_problems):
                results.append(str(all_problems[pos][1]))
            else:
                results.append('-1')
        elif x == -1:
            pos = bisect_right(all_problems, (L, -float('inf'))) - 1
            if pos >= 0:
                results.append(str(all_problems[pos][1]))
            else:
                results.append('-1')

print("\n".join(results))