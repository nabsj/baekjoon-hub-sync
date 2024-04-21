def self_number(n):
    num = n
    list = str(num)
    for i in list:
        num += int(i)
    return num

list = [i for i in range(1, 10001)]

for o in range(1, 10001):
    if self_number(o) in list:
        list.remove(self_number(o))

for p in range(len(list)):
    print(list[p])