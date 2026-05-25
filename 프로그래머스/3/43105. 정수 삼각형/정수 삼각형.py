# 동적계획법
# 현재 노드 + 이후노드 같은 경우 left, right 중 최대값

def solution(triangle):
    dp = [[0] * (i+1) for i in range(len(triangle))]
    dp[0][0] = triangle[0][0]
    
    for i in range(1, len(triangle)):
        for j in range(i + 1):
            if j == 0: # 왼쪽일때
                dp[i][j] = dp[i - 1][j] + triangle[i][j]
            elif j == i: # 오른쪽 일때
                dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
            else:
                dp[i][j] = max(dp[i - 1][j - 1], dp[i-1][j]) + triangle[i][j]
    
    return max(dp[-1])