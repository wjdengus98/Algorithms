# 백준 알고리즘 - 섬의 개수
# https://www.acmicpc.net/problem/4963
# BFS를 이용한 섬의 개수 세기

def BFS(x,y): 
    queue = [(x,y)]
    graph[x][y] = 0
    dx = [-1,1,0,0,-1,-1,1,1]
    dy = [0,0,-1,1,-1,1,-1,1]
    
    while queue:
        x,y = queue.pop(0)
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx,ny))


while True:
    w,h = map(int,input().split())
    if (w,h) == (0,0):
        break
    graph = [list(map(int,input().split())) for _ in range(h)]
    cnt = 0
    
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1: # 섬을 발견했음
                # BFS를 이용하여 섬을 탐색 
                BFS(i,j)
                cnt += 1 # 섬의 개수 증가
    
    print(cnt)
    