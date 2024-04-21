N = int(input())

num = 1

i = 1
while num < N and N != 1:
    num += 6*i
    #print("num", num)
    i += 1
    #print("i", i)

print(i)