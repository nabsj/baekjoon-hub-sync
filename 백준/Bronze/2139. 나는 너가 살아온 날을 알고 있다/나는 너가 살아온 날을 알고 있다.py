import sys

input = sys.stdin.readline

normal = [31,28,31,30,31,30,31,31,30,31,30,31]
yoon = [31,29,31,30,31,30,31,31,30,31,30,31]

while True:
    date = list(map(int, input().split()))

    if date[0] == 0:
        break

    yoon_nun = False
    if date[2] % 4 == 0:
        if date[2] % 100 == 0:
            if date[2] % 400 == 0:
                yoon_nun = True
        else:
            yoon_nun = True

    
    if not yoon_nun:
        month = sum(normal[:(date[1]-1)])
        print(month + date[0])
    else:
        month = sum(yoon[:(date[1]-1)])
        print(month + date[0])



    