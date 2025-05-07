# 백준 알고리즘 - 2644번
# 촌수계산
# https://www.acmicpc.net/problem/2644

from collections import deque

n = int(input()) # 사람 수
x,y = map(int,input().split()) # 촌수를 계산할 두 사람
m = int(input()) # 관계의 수
    
graph = [[] for _ in range(n+1)] # 사람 수 + 1 만큼의 그래프 생성

for _ in range(m):
    a,b = map(int,input().split())
    # 양방향 그래프이므로 두 사람 모두 연결
    graph[a].append(b) 
    graph[b].append(a)

visited = [False] * (n+1) # 방문 여부를 체크하기 위한 리스트
queue = deque() # BFS를 위한 큐
queue.append([x,0])
visited[x] = True # 시작 노드 방문 처리

while queue:
    curr, dist = queue.popleft() # 현재 노드와 거리
    if curr == y: # 도착 노드에 도달했을 때
        print(dist) # 촌수 출력
        break
    for next in graph[curr]: # 현재 노드와 연결된 노드들
        if not visited[next]: #
            visited[next] = True # 방문 처리
            queue.append([next, dist+1]) # 다음 노드와 거리 + 1
        else: # 이미 방문한 노드일 경우
            continue # 방문 처리 하지 않음
else:
    print(-1)
        
            
            
            