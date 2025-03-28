# 백준 알고리즘 - 11053번
# 가장 긴 증가하는 부분 수열

n = int(input())

numbers = list(map(int, input().split()))

dp = [1] * n
# dp[i] = i번째 수를 마지막으로 하는 가장 긴 증가하는 부분 수열의 길이

# dp[0] = 1 # 첫번째 수는 항상 1이다.
for i in range(1, n):
    for j in range(i):
        if numbers[i] > numbers[j] and dp[i] < dp[j] + 1: ## i번째 수가 j번째 수보다 크고, i번째 수의 길이가 j번째 수의 길이보다 1이 더 크면
            # i번째 수를 마지막으로 하는 가장 긴 증가하는 부분 수열의 길이를 구한다.
            dp[i] = dp[j] + 1
            
max_num = -1 # dp[i]의 최댓값을 구한다.
for k in range(n): 
    if max_num < dp[k]:
        max_num = dp[k]
print(max_num)
