import sys

data = sys.stdin.read().strip().split('\n')

dict = {}
count = 0

for i in data:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1
    count += 1


per = {key: (value / count * 100) for key, value in dict.items()}

for species in sorted(per):
    print(f"{species} {per[species]:.4f}")