#백준 알고리즘 1138번
# 한 줄로 서기

n = int(input()) # 사람 수

line = list(map(int, input().split())) # 왼쪽에 몇명이 있나
res = [0] * n # 결과 리스트

for i in range(1,n+1): # 1부터 n까지
    cnt = line[i-1] # 왼쪽에 몇명이 있나
    for j in range(n): # 0부터 n-1까지
        if cnt == 0 and res[j] == 0: # 왼쪽에 아무도 없고, j번째 자리가 비어있으면
            res[j] = i # j번째 자리에 i를 넣는다
            break
        elif res[j] == 0: # j번째 자리가 비어있으면
            cnt -= 1 # 왼쪽에 있는 사람 수를 1 줄인다

print(*res)
    