import sys
input = sys.stdin.read().split()

N = int(input[0])
now = list(map(int, input[1]))
target = list(map(int, input[2]))

copy_now = now[:]  # 복사본

def push(bulb, switch_idx, N):
    for i in range(max(0, switch_idx - 1), min(N, switch_idx + 2)):
        bulb[i] = 1 - bulb[i]

def func1(bulb, target_bulb, N):
    res = 0
    # target과 다르면 푸시
    for i in range(1, N):
        if bulb[i - 1] != target_bulb[i - 1]:
            push(bulb, i, N)
            res += 1

    # 최종 결과가 target과 같은지 확인
    for i in range(N):
        if bulb[i] != target_bulb[i]:
            return False, res

    return True, res

# 0번 스위치를 안 눌렀을 때
success, now_res = func1(now, target, N)
res = now_res if success else -1

# 0번 스위치를 눌렀을 때
push(copy_now, 0, N)
now_res = 1
success, result = func1(copy_now, target, N)
if success:
    now_res += result
    if res == -1 or now_res < res:
        res = now_res

print(res)