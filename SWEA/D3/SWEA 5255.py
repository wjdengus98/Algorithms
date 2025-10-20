# SWEA 5255 - 타일 붙이기
# DP (Dynamic Programming)

T = int(input())

dp = [0] * 31
dp[1] = 1
dp[2] = 3
dp[3] = 6

# 점화식: dp[i] = dp[i-1] + 2 * dp[i-2] + dp[i-3]
for i in range(4, 31):
    dp[i] = dp[i - 1] + 2 * dp[i - 2] + dp[i - 3]

for tc in range(1, T + 1):
    n = int(input())
    print(f"#{tc} {dp[n]}")
