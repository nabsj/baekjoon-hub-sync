import math
import sys

xA, yA, xB, yB, xC, yC = map(int, sys.stdin.read().split())

A = (xA, yA)
B = (xB, yB)
C = (xC, yC)

D1 = (xA + (C[0] - B[0]), yA + (C[1] - B[1]))
D2 = (xB + (A[0] - C[0]), yB + (A[1] - C[1]))
D3 = (xC + (B[0] - A[0]), yC + (B[1] - A[1]))

def dist(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def cal_round(p1, p2, p3, p4):
    return dist(p1, p2) + dist(p2, p3) + dist(p3, p4) + dist(p4, p1)

def linear(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) == (p3[0] - p1[0]) * (p2[1] - p1[1])

if linear(A, B, C):
    print(-1.0)
else:
    rounds = [
        cal_round(A, B, C, D1),
        cal_round(A, C, B, D2),
        cal_round(B, A, C, D3)
    ]
    
    min_round = min(rounds)
    max_round = max(rounds)
    
    print(max_round - min_round)