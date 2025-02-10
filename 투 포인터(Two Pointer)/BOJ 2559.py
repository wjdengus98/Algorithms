#백준 알고리즘
# 2559번 - 수열

n, k = map(int,input().split()) #n개의 정수, k개의 합
arr = list(map(int,input().split())) #n개의 정수
total = sum(arr[:k]) #k개의 합

max_total = total #최대값

for i in range(1, n-k + 1): #n-k번 반복
    total = total - arr[i - 1] + arr[i+k-1] #이전 합에서 첫번째 수를 빼고, k번째 수를 더한다
    max_total = max(max_total, total) #최대값 갱신

print(max_total)