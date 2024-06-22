import sys

input = list(map(int, sys.stdin.read().split()))

N = input[0]

a_lst = input[1:]

base_stick = sum(a_lst)

def cut(arr, reverses=False):
    sort_arr = sorted(arr, reverse=reverses)

    total = 0
    stick = base_stick
    for i in sort_arr:
        total += (stick - i) * i
        stick -= i
    return total

print(cut(a_lst))