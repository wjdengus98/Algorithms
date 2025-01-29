from collections import deque

# 이동 방향 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(x, y):
    queue = deque([(x, y)])
    graph[x][y] = 0  # 방문 처리
    cnt = 1  # 시작 지점 포함

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위를 벗어나지 않고, 음식물이 있는 경우
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                graph[nx][ny] = 0  # 방문 처리
                queue.append((nx, ny))
                cnt += 1  # 음식물 크기 증가

    return cnt  # 음식물 덩어리 크기 반환

# 입력 받기
n, m, k = map(int, input().split())
graph = [[0] * m for _ in range(n)]  # 2차원 리스트 (0 = 빈 공간)

# 음식물 위치 입력
for _ in range(k):
    r, c = map(int, input().split())
    graph[r-1][c-1] = 1  # 음식물이 있는 위치 = 1

# 가장 큰 음식물 크기 찾기
max_size = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:  # 음식물이 있으면 BFS 실행
            max_size = max(max_size, BFS(i, j))

print(max_size)
