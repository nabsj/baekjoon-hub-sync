import sys

N = int(sys.stdin.read()) % 6
# 1 + 1 = 2
# 1 + 3 = 4
# 3 + 1 = 4
# 3 + 3 = 6 -> 7, 9(상근 우승)


if N == 5:
    print('SK')
elif N == 4:
    print('CY')
elif N == 3:
    print('SK')
elif N == 2:
    print('CY')
elif N == 1:
    print('SK')
elif N == 0:
    print('CY')