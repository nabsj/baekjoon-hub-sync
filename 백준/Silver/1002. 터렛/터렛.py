import sys

T = int(sys.stdin.readline())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    dis = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    # 같은 위치, 같은 반지름
    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
    elif dis > r1 + r2:  # 두 원이 서로 떨어져 있을 때
        print(0)
    elif dis == r1 + r2:  # 두 원이 외접할 때
        print(1)
    elif dis < abs(r1 - r2):  # 한 원이 다른 원 안에 있고 내접하지 않을 때
        print(0)
    elif dis == abs(r1 - r2):  # 한 원이 다른 원 안에서 내접할 때
        print(1)
    else:  # 두 원이 두 점에서 만날 때
        print(2)
