import sys
from fractions import Fraction

input = sys.stdin.read

data = input().split()
index = 0

T = int(data[index])
index += 1

results = []

for _ in range(T):
    N = int(data[index])
    M = int(data[index + 1])
    index += 2

    total_snacks = [Fraction(0) for _ in range(N)]

    for __ in range(M):
        Vj = int(data[index])
        Aj = list(map(int, data[index + 1:index + 1 + N]))
        index += 1 + N

        for i in range(N):
            if Vj > 0:
                total_snacks[i] += Fraction(Aj[i], Vj)

    max_snacks = max(total_snacks)
    min_snacks = min(total_snacks)

    diff = max_snacks - min_snacks

    if diff.denominator == 1:
        results.append(f"{diff.numerator}\n")
    else:
        results.append(f"{diff.numerator}/{diff.denominator}\n")

sys.stdout.write("".join(results))

