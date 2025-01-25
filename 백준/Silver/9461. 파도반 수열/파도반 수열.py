#파도반 수열
# 다이나믹 프로그래밍

t = int(input())

for i in range(t):
    n = int(input())
    
    if n == 1 or n == 2 or n == 3:
        print(1)
    elif n == 4 or n == 5:
        print(2)
    elif n == 6:
        print(3)
    else:
        dp = [0] * (n+1) # dp 테이블 설정
        
        dp[1] = 1
        dp[2] = 1
        dp[3] = 1
        dp[4] = 2
        dp[5] = 2
        dp[6] = 3
        
        for j in range(7, n+1):
            dp[j] = dp[j-1] + dp[j-5] # 점화식
        
        ans = dp[n]
        print(ans)
