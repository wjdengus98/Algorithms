# 백준 알고리즘 - 2178번
# 미로 탐색

from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

# BFS 소스코드 구현
def bfs(x,y):
    queue = deque() # 큐 생성
    queue.append((x,y)) # 시작 노드를 큐에 삽입
    
    while queue: # 큐가 빌 때까지 반복
        x, y = queue.popleft() # 큐에서 하나의 원소를 뽑아 출력
        
        for i in range(4): # 현재 위치에서 4가지 방향으로의 위치 확인
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m: # 미로 찾기 공간을 벗어난 경우 무시
                continue
            
            if graph[nx][ny] == 0: #벽인 경우, 무시시
                continue
            
            if graph[nx][ny] == 1: # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
                graph[nx][ny] = graph[x][y] + 1 # 최단 거리 기록
                queue.append((nx,ny)) # 큐에 삽입
                
    return graph[n-1][m-1] # 가장 오른쪽 아래까지의 최단 거리 반환

n, m = map(int,input().split()) # n: 세로, m: 가로

graph = [] # 미로 정보 입력

for i in range(n):  
    graph.append(list(map(int,input())))

print(bfs(0,0)) # BFS 수행 결과 출력
    

