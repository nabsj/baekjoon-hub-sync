import sys

S = sys.stdin.read()

count_a = 0
count_b = 0
count_c = 0

for char in S:
    if char == 'a':
        count_a = (count_a * 2 + 1) % 1000000007
    elif char == 'b':
        count_b = (count_b * 2 + count_a) % 1000000007
    elif char == 'c':
        count_c = (count_c * 2 + count_b) % 1000000007

print(count_c)