#4835. [파이썬 S/W 문제해결 기본] 1일차 구간합

T = int(input())

for i in range(T):
    n,m = map(int,input().split())
    nums = list(map(int,input().split()))

    total = []

    for j in range(n-m + 1):
        tot =0
        for k in range(m):
            tot += nums[j + k]
        total.append(tot)
        
    print(f"#{i+1} {max(total) - min(total)}")
