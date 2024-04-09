import sys
input = sys.stdin.readline().strip()

#res = [] #결과
res = set()

check_left = []
pair = []

for i, char in enumerate(input):
    #print(input[i])
    if char == '(':
        check_left.append(i)
    elif char == ')':
        left = check_left.pop()
        pair.append((left, i))

#print(check_left)
#print(check_right)
#print(pair)
'''
#index는 재귀호출 깊이 확인용
def gen(index, seq):
    print(index, "시작", seq)
    if index == len(pair):
        res.add(seq)
        return
    
    gen(index + 1, seq)

    left, right = pair[index]
    #print((left, right))

    ############문자열만 어캐하면됌#########
    new_seq = seq[:left] + seq[left+1:right] + seq[right+1:]
    print(new_seq)
    #print(new_seq)
    gen(index + 1, new_seq)

gen(0, input)
'''
def gen(index, seq, removed):
    if index == len(pair):
        res.add("".join([seq[i] for i in range(len(seq)) if i not in removed]))
        return
    
    # 괄호 쌍을 제거하지 않는 경우
    gen(index + 1, seq, removed)
    
    # 현재 괄호 쌍을 제거하는 경우
    left, right = pair[index]
    new_removed = removed.union({left, right})
    gen(index + 1, seq, new_removed)

gen(0, input, set())

list = sorted(res)
# 결과 정렬 및 출력
for seq in list[1:]:
    print(seq)
