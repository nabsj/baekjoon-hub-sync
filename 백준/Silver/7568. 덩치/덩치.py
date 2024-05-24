N = int(input().strip())
people = []

for _ in range(N):
    x, y = map(int, input().split())
    people.append((x, y))

ranks = [1] * N

for i in range(N):
    for j in range(N):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            ranks[i] += 1

print(' '.join(map(str, ranks)))