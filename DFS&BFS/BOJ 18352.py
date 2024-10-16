from collections import deque
import sys

n,m,k,x = map(int, input().split()) #도시개수, 도로개수,거리 정보, 출발 도시

input = sys.stdin.readline #더 빠른 입력 함수 사용

graph = [[] for _ in range(n+1)] 

#도로 정보 입력
for _ in range(m):
    a,b = map(int, input().split())
    
    graph[a].append(b) #단방향 그래프
    
     
dist = [-1] * (n+1) #각 노드까지의 최단 거리를 저장할 리스트(-1로 초기화)
dist[x] = 0 #출발 도시의 거리는 0으로 설정

#BFS 큐 초기화
q = deque([x])

while q:
    now = q.popleft() #현재 노드를 pop한다
    for i in graph[now]: #현재 노드를 탐색한다
        if dist[i] == -1: #방문을 하지 않았으면
            dist[i] = dist[now] + 1
            q.append(i)

flag = False
for i in range(1,n+1):
    if dist[i] == k:
        print(i)
        flag = True


if flag == False:
    print("-1")