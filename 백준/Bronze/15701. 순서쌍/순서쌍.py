import math

N = int(input())

count = 0
for i in range(1, int(math.sqrt(N))+1):
    if N % i == 0:
        if i == int(N/i):
            count += 1
        else:
            count += 2
        
print(count)