#SWEA 최장 경로

T = int(input())

def dfs(curr, visit):
    global ans
    
    ans = max(ans, len(visit)) #최대값 갱신
    
    for node in graph[curr]: #노드에 연결된 모든 그래프 탐색
        if node not in visit: #방문하지 않았다면
            dfs(node, visit + [node]) #그 다음 노드 방문 및 길이 업데이트
    

for i in range(T):
    n,m = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        x,y = map(int,input().split())
        #무방향 그래프이므로 양방향으로 연결
        graph[x].append(y)
        graph[y].append(x)
    
    ans = 0
    for s in range(1, n+1):
        dfs(s, [s])
    
    print(f"{i+1} {ans}")