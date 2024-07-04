import sys
import re

input = sys.stdin.read()

res = []

def cutfunc(str):
    return str[1:-1]
def cleanhtml(str):
    clean = re.compile('<.*?>')
    return re.sub(clean,'', str)

i=0
while i < len(input):
    if input[i] == '<':
        end = input.find('>', i)
        
        tag = input[i+1:end]
        tag_lst = tag.split('=')
        if len(tag_lst) > 1:
            res.append('title : '+ cutfunc(tag_lst[1]))
    
        if tag == 'p':
            start_idx = i
        elif tag =='/p':
            end_idx = i
            par = input[start_idx:end_idx]
            res.append(cleanhtml(par))
        
    i+=1

for p in res:
    print(re.sub(' +', ' ', p))