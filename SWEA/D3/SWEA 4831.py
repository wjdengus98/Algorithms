#[S/W 문제해결 기본] - 전기버스

T = int(input())

for i in range(T):
    k, n, m = map(int,input().split())
    cnt = 0 #충전 횟수
    chargers = list(map(int, input().split()))

    start = end = 0 #버스의 현재위치와 마지막 위치

    while start + k < n:
        next = -1
        for station in chargers:
            if end < station <= start + k:
                next = station

        # 충전할 수 없는 경우 (종점에 도달할 수 없는 경우)     
        if next == -1:
            cnt = 0
            break
        
         # 충전한 위치를 업데이트하고 충전 횟수 증가
        start = next
        end = next
        cnt += 1

 
    print(f"#{i+1} {cnt}")