def sugar(N):
    # 5kg 봉지로만 구성할 때의 최대 개수부터 시작
    for five_bags in range(N // 5, -1, -1):
        # 남은 무게
        remaining_weight = N - (five_bags * 5)
        # 남은 무게가 3kg 봉지로 정확하게 나누어 떨어지는 경우
        if remaining_weight % 3 == 0:
            three_bags = remaining_weight // 3
            return five_bags + three_bags
    # 모든 경우를 시도한 후에도 정확한 N킬로그램을 만들 수 없는 경우
    return -1

    
N = int(input())
print(sugar(N))