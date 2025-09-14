# 백준 10709번
# 기상캐스터

H,W = map(int,input().split())
arr = [input() for _ in range(H)]
v = [[0] * W for _ in range(H)]

for i in range(H):
    cnt = -1 #'c'를 못만났으면 계속 -1
    for j in range(W):
        if arr[i][j] == 'c': # 'c'를 만났으면 0으로 초기화
            cnt = 0
        else: #구름을 만났다면 1씩 증가
            if cnt >= 0:
                cnt += 1
        v[i][j] = cnt

for lst in v:
    print(*lst)
                
      
            