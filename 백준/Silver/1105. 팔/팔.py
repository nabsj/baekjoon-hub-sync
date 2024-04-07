import sys

l, r = sys.stdin.readline().split()
cnt = 0

# 자연수의 길이가 다르면 8을 포함하지 않는 자연수가 존재
if len(l) != len(r):
    print(cnt)

else:
    # 두 자연수의 자릿수를 확인
    for i in range(len(l)):
        # 두 자연수의 자릿수의 값이 8로 같으면 무조건 8을 포함하므로 카운트한다.
        if l[i] == r[i] == "8":
            cnt += 1

        # 두 자연수의 자릿수의 값이 다르면 8을 세지 않아도 되므로 멈춘다.
        if l[i] != r[i]:
            break

    print(cnt)