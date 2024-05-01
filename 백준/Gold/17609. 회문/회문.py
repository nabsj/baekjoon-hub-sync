import sys

input = sys.stdin.read().split()

T = int(input[0])

#판별
def discr(string):
    if string == string[::-1]:
        return print('0')
    
    left, right = 0, len(string) - 1
    while left < right:
        if string[left] != string[right]:
            # 왼쪽문자 제거, 오른쪽으로 한칸이동
            if string[left+1 : right+1] == string[left+1:right+1][::-1]:
                return print('1')
            # 오른쪽문자 제거, 슬라이싱
            if string[left: right] == string[left:right][::-1]:
                return print('1')
            
            return print('2')
        left += 1
        right -= 1
    
idx = 1
for _ in range(T):
    discr(input[idx])
    idx += 1