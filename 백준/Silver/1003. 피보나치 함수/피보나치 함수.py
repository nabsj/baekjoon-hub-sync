def fibonacci_count(max_n):
    count = [[0, 0] for _ in range(max_n + 1)]
    
    count[0] = [1, 0]  # F(0)
    if max_n > 0:
        count[1] = [0, 1]  # F(1)
    
    for i in range(2, max_n + 1):
        count[i][0] = count[i-1][0] + count[i-2][0]
        count[i][1] = count[i-1][1] + count[i-2][1]
    
    return count

max_value = 40
counts = fibonacci_count(max_value)

T = int(input().strip())

results = []
for _ in range(T):
    N = int(input().strip())
    results.append(f"{counts[N][0]} {counts[N][1]}")

for res in results:
    print(res)