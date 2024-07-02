import sys
input = sys.stdin.readline

N, C = map(int, input().split())  # 마을 수 N, 트럭 용량 C
M = int(input())  # 박스 정보 개수 M

lst = []
for _ in range(M):
    start, end, box_count = map(int, input().split())
    lst.append((start, end, box_count))

lst.sort(key=lambda x: (x[1], x[0]))

tackbae_box = [0] * (N + 1) # 마을별 트럭에 실려있는 박스수

total = 0
for start, end, box_count in lst:
    load = min(box_count, C - max(tackbae_box[start : end]))
    
    for i in range(start, end):
        tackbae_box[i] += load
    
    total += load

print(total)
