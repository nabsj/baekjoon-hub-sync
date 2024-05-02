import sys

input = sys.stdin.read().split()

N = int(input[0])

saved_dict = {}

for i in range(1, N+1):
    file_name = input[i].split('.')
    if file_name[-1] in saved_dict:
        saved_dict[file_name[-1]] += 1
    else:
        saved_dict[file_name[-1]] = 1
    
for k, v in sorted(saved_dict.items()):
    print(k, v)