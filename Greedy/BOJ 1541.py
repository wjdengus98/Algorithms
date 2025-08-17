# 백준 알고리즘 - 잃어버린 괄호
# 1541번

def mysum(k): # '+'로 구분해서 더해주는 함수
    B = k.split('+') # '+' 구분
    cnt = 0 # 더할 변수
    for j in B:
        cnt += int(j) # +까지 이어진 부분 전부 더함
        

answer = 0
# 입력받은 수식을 '-' 기준으로 분리
# 예: "55-50+40" → ["55", "50+40"]
A = input().split("-")

# 첫 번째 그룹은 그냥 더하고, 그 이후 그룹들은 모두 뺌
for i in range(len(A)):
    res = mysum(A[i]) #각 그룹의 + 구분된 부분 계산
    if i == 0: #첫번째 그룹
        answer += res # 더하기
    else: # 남은 그룹
        answer -= res # 빼기

print(answer) #출력