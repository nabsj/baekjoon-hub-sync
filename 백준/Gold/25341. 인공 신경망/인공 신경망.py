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
out_w_lst, out_b_lst = output[:M], output[M]

# print(out_w_lst, out_b_lst)

# 은닉층 최종가중치
hidden_final = [0] * N

hidden_final_b = out_b_lst

for i in range(M):
    for j in range(len(p_lst[i])):
        hidden_final[p_lst[i][j] - 1] += w_lst[i][j] * out_w_lst[i]
    hidden_final_b += b_lst[i] * out_w_lst[i]

for _ in range(Q):
    input_query = list(map(int, input().split()))
    
    total_w_input = 0
    for p in range(N):
        total_w_input += (input_query[p] * hidden_final[p])
    print(total_w_input + hidden_final_b)