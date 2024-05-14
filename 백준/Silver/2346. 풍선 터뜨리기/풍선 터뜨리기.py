N = int(input())
balloon_values = list(map(int, input().split()))

balloons = list(range(1, N + 1))
result = []
idx = 0

while balloons:
    current = balloons.pop(idx)
    result.append(current)

    move = balloon_values[current - 1]
    if move > 0:
        move -= 1

    if balloons:
        idx = (idx + move) % len(balloons)

print(*result)