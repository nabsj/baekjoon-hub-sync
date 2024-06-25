def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])  # 전화기의 개수
    phones = list(map(int, data[1:]))  # 각 전화기가 연결된 전화기 번호 리스트
    
    cnt = 0  # 변경된 착신 전환 수
    
    for i in range(N):
        if phones[i] == i + 1:  # 자기 자신으로 연결된 경우, 다음 번호로 변경
            if i + 1 < N:  # 다음 번호가 범위 안에 있는 경우
                phones[i] = i + 2
            else:  # 마지막 번호인 경우 1번으로 연결
                phones[i] = 1
            cnt += 1
    
    # 결과 출력
    print(cnt)
    print(" ".join(map(str, phones)))

if __name__ == "__main__":
    main()
