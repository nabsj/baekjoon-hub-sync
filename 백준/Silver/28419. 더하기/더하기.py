import sys
input = sys.stdin.read

data = input().split()
N = int(data[0])
lst = list(map(int, data[1:]))

odd_sum = sum(lst[i] for i in range(0, N, 2))
even_sum = sum(lst[i] for i in range(1, N, 2))
diff = odd_sum - even_sum

if diff == 0:
    print(0)
else:
    if N <=3 and N % 2 == 1 and odd_sum > even_sum:
        print(-1)
    elif N <=3 and N % 2 == 0 and odd_sum < even_sum:
        print(-1)
    else:
        print(abs(odd_sum-even_sum))
