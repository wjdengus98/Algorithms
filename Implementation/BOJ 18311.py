n,k = map(int,input().split()) #n,k 입력

road = list(map(int,input().split())) #도로 출력

total = sum(road) #도로 총합 계산


if k < total: #이동 거리가 직선 거리보다 작을 때
    for i in range(n):
        k -= road[i]
        if k < 0:
            print(i+1)
            break 
        
else: #이동거리가 직선거리보다 클 때 
    dist = (k - total)
    for i in range(n-1,-1,-1):       
        dist -= road[i]
        if dist < 0:
            print(i+1)
            break
        