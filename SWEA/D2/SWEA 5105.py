#파이썬 S/W 문제해결 기본] 6일차 - 미로의 거리

from collections import deque

# 이동 방향 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(x,y):
    q = deque() # 큐 생성
    v = [[0] * n for _ in range(n)] # 방문 처리를 위한 2차원 리스트 생성
    
    q.append([x,y]) # 시작점을 큐에 넣음
    v[x][y] = 1 # 시작점 방문 처리
    
    while q: # 큐가 빌 때까지 반복
        x, y = q.popleft() # 큐에서 좌표를 꺼냄

        for i in range(4): # 상하좌우 이동
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 범위를 벗어나거나 벽인 경우
            if nx < 0 or nx >= n or ny < 0 or ny >= n or maze[nx][ny] == 1: 
                continue #다음 좌표로 나아감
            
            if maze[nx][ny] == 3: #목적지에 도달
                return v[x][y] - 1 #결과값 리턴
            
            if v[nx][ny] == 0: #0인 경우
                q.append([nx,ny]) # 큐에 좌표를 넣음
                v[nx][ny] = v[x][y] + 1 #방문 처리 및 이동거리
            
    return 0 #목적지에 도달하지 못한 경우 0을 리턴 

TC = int(input())

for tc in range(1, TC+1):
    n = int(input())
    maze = [list(map(int,input())) for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2: # 시작점
                x,y = i, j # 시작점 좌표 저장
    
    ans = BFS(x,y) # 시작점 좌표를 BFS 함수에 넣어서 결과값을 ans에 저장
    print(f"#{tc} {ans}") # 결과값 출력
      
    
    