# SWEA - 달팽이 숫자

T = int(input())
# 우하좌상 배열
di = [0,1,0,-1] # 우하좌상
dj = [1,0,-1,0] # 우하좌상

for tc in range(1, T+1):
    N = int(input()) # N*N 배열
    arr = [[0]*N for _ in range(N)] # N*N 배열 초기화
    
    i,j, cnt, dr = 0,0,1,0 # i,j: 현재 위치, cnt: 채울 숫자, dr: 방향
    arr[i][j] = cnt # 시작점에 1을 넣어줌
    cnt += 1 # 2부터 시작
    
    while cnt <= N*N: # cnt가 N*N보다 작거나 같을 때까지 반복
        ni, nj = i + di[dr], j + dj[dr] # 다음 위치
        if 0<=ni<N and 0<=nj<N and arr[ni][nj] == 0: # 다음 위치가 배열 안에 있고, 0이면
            i, j = ni, nj # 다음 위치로 이동
            arr[i][j] = cnt # 다음 위치에 cnt 넣어줌
            cnt += 1 # cnt 1 증가
        else: # 다음 위치가 배열 밖이거나, 이미 숫자가 채워져 있으면
            dr = (dr+1)%4 # 방향 전환
    print(f'#{tc}')
    for i in range(N):
        print(*arr[i])