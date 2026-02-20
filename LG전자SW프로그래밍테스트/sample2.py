# 완전탐색 시 시간초과
# 선택이 연속적으로 이어지므로 -> DP로 풀어야함.

N = int(input())
mushrooms = list(map(int,input().split()))

dp = [[0] * 2 for _ in range(N)]

dp[0][0] = mushrooms[0]  # 0번을 홀수 번째로 먹음
dp[0][1] = 0             # 0번을 안 먹음

for i in range(1, N):
    # i번을 안 먹고 이전 홀수 상태 유지, 짝수/안 먹은 상태에서 새로운 홀수 상태 먹기
    dp[i][0] = max(dp[i-1][0], dp[i-1][1] + mushrooms[i])
    
    # i번을 짝수를 먹고, 안 먹은 상태 유지. 홀수 먹은 상태에서 새로운 짝수 상태 먹기 
    dp[i][1] = max(dp[i-1][1], dp[i-1][0] - mushrooms[i])

print(max(dp[N-1]))