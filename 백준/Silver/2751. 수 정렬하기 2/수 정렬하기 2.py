import sys

input = sys.stdin.read().split()

N = int(input[0])

list = list(map(int, input[1:1+N]))
list2 = sorted(list)
for i in list2:
    print(i)