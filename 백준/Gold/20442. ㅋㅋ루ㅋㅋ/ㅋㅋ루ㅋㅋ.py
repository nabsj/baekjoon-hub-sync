text = input()

left_k, right_k = [], [] #R기준 쓸수 있는 K의 개수 저장
left_idx, right_idx = 0, 0 
for i in text:
    if i == 'K':
        left_idx += 1
    else:
        left_k.append(left_idx)

for i in text[::-1]:
    if i == 'K':
        right_idx += 1
    else:
        right_k.append(right_idx)
right_k.reverse()
#print(left_k, right_k)

left, right = 0, len(left_k) - 1
ans = 0

while left <= right:
    #print(right - left + 1, 2 * min(left_k[left], right_k[right]))
    ans = max(ans, (right - left + 1) + 2 * min(left_k[left], right_k[right]))
    
    if left_k[left] < right_k[right]:
        left += 1
    else:
        right -= 1
print(ans)

# 참고
# https://chanu-ps.tistory.com/24