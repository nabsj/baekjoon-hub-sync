import sys
input = sys.stdin.read

data = input().split()
    
N = int(data[0])  # 포켓몬 수
M = int(data[1])  # 문제 수

name_to_number = {}
number_to_name = {}

index = 2
for i in range(1, N+1):
    pokemon_name = data[index]
    name_to_number[pokemon_name] = i
    number_to_name[i] = pokemon_name
    index += 1

results = []
for _ in range(M):
    query = data[index]
    if query.isdigit():
        # 숫자면 포켓몬 이름 출력
        results.append(number_to_name[int(query)])
    else:
        # 이름이면 포켓몬 번호 출력
        results.append(str(name_to_number[query]))
    index += 1

# 결과 출력
sys.stdout.write("\n".join(results) + "\n")