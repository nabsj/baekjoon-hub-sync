import sys

input = sys.stdin.readline

T = int(input())

def rev(txt):
    res_tex = ''
    for i in range(len(txt)-1, -1, -1):
        res_tex += txt[i]
    return res_tex

def tail(txt):
    return str(txt[1:])

for _ in range(T):
    txt = input().strip()

    # S' 구하기
    S_dot_len = len(txt) // 3
    S_dot_len += (0 if len(txt) % 3 == 0 else 1)

    S_dot = txt[:S_dot_len]
    
    res_lst = []
    res_lst.append(S_dot + rev(S_dot) + S_dot)
    res_lst.append(S_dot + tail(rev(S_dot)) + S_dot)
    res_lst.append(S_dot + rev(S_dot) + tail(S_dot))
    res_lst.append(S_dot + tail(rev(S_dot)) + tail(S_dot))

    if txt in res_lst:
        print(1)
    else:
        print(0)