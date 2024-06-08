import sys

input = sys.stdin.read().split()

N = int(input[0])
idx = 0

dic = {}

for i in range(1, N+1):
    if input[i] in dic:
        dic[input[i]] += 1
    else:
        dic[input[i]] = 1

max_count = max(dic.values())
most_books = [i for i, count in dic.items() if count == max_count]

print(sorted(most_books)[0])