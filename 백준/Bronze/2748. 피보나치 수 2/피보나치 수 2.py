n = int(input())

list = []

list.append(0)
list.append(1)

for i in range(2, n+1):
    list.append(list[i-1] + list[i-2])

print(list.pop())