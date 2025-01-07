# 알고리즘 수업 - 깊이 우선 탐색
# 백준 24479번

import sys
sys.setrecursionlimit(150000) # 재귀 깊이 제한 늘리기

def dfs(node):
    global order
    visited[node] = order  # 현재 노드 방문 순서 기록
    graph[node].sort()  # 인접 리스트 정렬 (탐색 순서 보장)
    for i in graph[node]:
        if visited[i] == 0:  # 아직 방문하지 않은 노드라면
            order += 1
            dfs(i)

# 입력 처리
N, M, R = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]  # 인접 리스트 생성
visited = [0] * (N + 1)  # 방문 순서 기록
order = 1  # 방문 순서 초기화

# 간선 정보 입력
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)  # 양방향 간선 추가
    graph[b].append(a)

# DFS 실행
dfs(R)

# 방문 순서 출력
for i in range(1, N + 1):
    print(visited[i])
