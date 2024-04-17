import sys

def get_median(input_num): #홀수만 들어감
	input_num.sort()
	return(input_num[(len(input_num)//2)])

input = sys.stdin.read().split()

T = int(input[0])

index = 1
for _ in range(T):

    res = []
    list = []
    
    for i in range(int(input[index])):
        index += 1
        list.append(int(input[index]))

        if (i+1) % 2 ==1:
              res.append(int(get_median(list)))
    index += 1
    
    print(len(res))
    
    if len(res) > 10:
        for i in range(0, len(res), 10):
            print(*res[i:i+10])
    else:
        print(*res)