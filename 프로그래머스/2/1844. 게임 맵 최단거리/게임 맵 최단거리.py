from collections import deque

# 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    
    queue = deque()
    queue.append((0,0,1)) #행, 열, 거리
    
    while queue:
        x,y,dist = queue.popleft()
        
        if x == n-1 and y == m-1: # 끝에 도달하면 
            return dist #거리 반환
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽인 경우 무시
            if maps[nx][ny] == 0:
                continue
            #방문 체크
            if visited[nx][ny] == False:
                visited[nx][ny] = True
                queue.append((nx,ny,dist+1))
    return -1 # 방문 할 수 없는 경우 -1 