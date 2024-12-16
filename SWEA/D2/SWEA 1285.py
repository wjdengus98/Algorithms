#아름이의 돌 던지기

T = int(input())

for i in range(T):
    n = int(input())
    location = list(map(int,input().split()))
    
    min_dist = float('Inf')
    cnt = 0
    
    for l in location:
        dist = abs(l)

        if min_dist > dist:
            min_dist = dist
            cnt = 1
        
        elif dist == min_dist:
            cnt += 1
        
    
    print(f"#{i+1} {min_dist} {cnt}") 