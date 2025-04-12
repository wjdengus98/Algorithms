# 백준 알고리즘 - 1912번
# 연속합

n = int(input()) # 배열 크기 n

arr = list(map(int, input().split())) # 배열 arr
dp = [0] * n # dp 테이블 설정

dp[0] = arr[0] # 첫 번째 원소는 그대로 저장
 
for i in range(1, n):
    if dp[i - 1] < 0: # dp[i - 1]이 음수일 경우
        dp[i] = arr[i] # dp[i]에 arr[i]를 저장
    else: # dp[i - 1]이 양수일 경우
        dp[i] = dp[i - 1] + arr[i] # dp[i]에 arr[i]를 더해서 저장
      
max_Num = -1001

for i in range(n): #dp 테이블 순회하면서 최대값 찾기
    if max_Num < dp[i]:
        max_Num = dp[i]
        
print(max_Num)
