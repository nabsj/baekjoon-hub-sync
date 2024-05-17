import sys

cro_alp = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

input_text = sys.stdin.read().strip()

idx = 0
count = 0

while idx < len(input_text):
    if idx <= len(input_text) - 3 and input_text[idx:idx+3] in cro_alp:
        idx += 3
    elif idx <= len(input_text) - 2 and input_text[idx:idx+2] in cro_alp:
        idx += 2
    else:
        idx += 1

    count += 1
print(count)
