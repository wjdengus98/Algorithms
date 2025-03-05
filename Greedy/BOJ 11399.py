# 백준 알고리즘 - 11399번
# ATM

n = int(input()) # 사람의 수
p = list(map(int, input().split())) # 각 사람이 돈을 인출하는데 걸리는 시간
sum_list = [0] * (n) # 각 사람이 돈을 인출하는데 걸리는 시간의 합

p.sort() # 오름차순 정렬

for i in range(n):
    sum_list[i] = sum(p[:i+1]) # 누적 시간의 합 배열 생성

total = sum(sum_list) #누적 시간의 총합

print(total) #출력