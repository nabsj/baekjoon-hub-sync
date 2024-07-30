def find_competition_name(N, M, S):
    # 자음 집합
    consonants = set("BCDFGHJKLMNPQRSTVWXYZ")
    # 마지막부터 탐색하여 AA<자음> 패턴 찾기
    i = N - 3
    while i >= 0:
        if S[i] == 'A' and S[i+1] == 'A' and S[i+2] in consonants:
            # 만약 현재 위치에서 길이 M을 만족하는 이름을 만들 수 있다면
            start_index = i + 3 - M
            if start_index >= 0:
                # 결과적으로 가능한 이름
                T = S[start_index:start_index + M]
                return "YES", T
        i -= 1
    return "NO", None

# 입력 받기
N, M = map(int, input().split())
S = input()

# 함수 실행
result, competition_name = find_competition_name(N, M, S)
print(result)
if result == "YES":
    print(competition_name)
