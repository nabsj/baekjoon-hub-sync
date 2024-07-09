

#### LDS(Longest Decreasing Subsequence) 최장 감소 부분 수열

N = int(input().strip())
lst = list(map(int, input().strip().split()))

dp = [1] * N 
# 각요소를 포함하는 LDS의 최소 길이는 자기 포함이므로 1로 초기화

for i in range(N):
    for j in range(i):
        #print('i는 :', lst[i],'j는 :', lst[j])
        if lst[j] > lst[i]:
            #print(dp[i], dp[j] + 1)
            dp[i] = max(dp[i], dp[j] + 1)

max_LDS = max(dp)
#print(dp)
print(N - max_LDS)
