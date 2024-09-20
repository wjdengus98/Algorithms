#백준 2606 바이러스

n = int(input()) #컴퓨터의 수
m = int(input()) #컴퓨터 네트워크의 수

graph = [[] for _ in range(n+1)]
# graph[1] = []
# graph[2] = []

visited = [0 for _ in range(n+1)] #방문여부 확인

#visited[1] = 0 #방문하지 않았으면 0
#visited[1] = 1 #방문하였다면 1

for _ in range(m):
    a,b = map(int, input().split())

    #양방향 그래프 연결
    graph[a].append(b)
    graph[b].append(a)

def dfs(node):
    visited[node] = 1 #첫번째 노드는 무조건 방문처리

    for nxt in graph[node]: #기존 그래프
        if visited[nxt] == 1: #노드를 방문했다면
            continue #건너뛴다. 
        dfs(nxt) #그래프와 연결된 노드들로 이동을 진행한다

dfs(1)

print(sum(visited) - 1) #1번 컴퓨터를 빼줘야 값이 나온다

