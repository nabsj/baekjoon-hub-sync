import heapq
import sys
from collections import defaultdict

N = int(sys.stdin.readline())

minHeap, maxHeap = [], []
solved = defaultdict(int)

for _ in range(N):
    P, L = map(int, input().split())
    heapq.heappush(minHeap, (L, P))
    heapq.heappush(maxHeap, (-L, -P))

M = int(input())
for _ in range(M):
    command = input().split()

    if command[0] == "recommend":
        # 어려운 문제 추천
        if command[1] == '1':
            while solved[abs(maxHeap[0][1])] != 0:
                solved[abs(maxHeap[0][1])] -= 1
                heapq.heappop(maxHeap)
            print(-maxHeap[0][1])
        # 쉬운 문제 추천
        else:
            while solved[minHeap[0][1]] != 0:
                solved[minHeap[0][1]] -= 1
                heapq.heappop(minHeap)
            print(minHeap[0][1])

    elif command[0] == "add":
        P = int(command[1])
        L = int(command[2])
        heapq.heappush(minHeap, (L, P))
        heapq.heappush(maxHeap, (-L, -P))

    elif command[0] == "solved":
        solved[int(command[1])] += 1