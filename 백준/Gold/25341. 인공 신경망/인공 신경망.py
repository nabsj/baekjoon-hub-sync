import sys

input = sys.stdin.readline

N, M, Q = map(int, input().split()) 
# 입력층 입력크기 N, 은닉층 인공신경개수 M, 출력값 계산 횟수 Q

p_lst, w_lst, b_lst = [], [], []

for _ in range(M):
    tmp = list(map(int, input().split()))
    C = tmp[0]
    
    idx = 1
    p_lst.append(tmp[idx : idx+C])
    w_lst.append(tmp[idx+C : idx + 2*C])
    b_lst.append(tmp[idx + 2*C])

# print(p_lst)
# print(w_lst)
# print(b_lst)

output = list(map(int, input().split()))
out_w_lst = output[:M]
out_b_lst = output[M]

# 출력층 가중치를 이용한 전처리
modified_weights = [0] * N  # 입력층의 각 입력에 대한 최종 가중치
modified_bias = out_b_lst   # 최종 출력층 편향

for i in range(M):
    # 은닉층 i의 각 입력에 대해 출력층 가중치를 곱하여 수정
    for j in range(len(p_lst[i])):
        p_index = p_lst[i][j] - 1
        modified_weights[p_index] += w_lst[i][j] * out_w_lst[i]
    # 은닉층 i의 편향값도 출력층 가중치와 편향값에 영향을 줌
    modified_bias += b_lst[i] * out_w_lst[i]

# 각 쿼리에 대해 최종 출력 계산
for _ in range(Q):
    inputs = list(map(int, input().split()))
    # 입력과 미리 계산된 가중치의 곱 및 편향 합산
    final_output = sum(inputs[j] * modified_weights[j] for j in range(N)) + modified_bias
    print(final_output)