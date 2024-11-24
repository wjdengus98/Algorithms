#4871 그래프 경로

def dfs(node):
    visited[node] = 1
    #print(visited)
    for i in graph[node]:
        if visited[i] == 0:
            dfs(i)

t = int(input())

for i in range(t):
    v,e = map(int,input().split())
    graph = [[] for _ in range(v+1)]
    
    visited = [0] * (v+1)
    for j in range(e):
        start,end = map(int,input().split())
        graph[start].append(end)
    
    s,g = map(int,input().split())
    dfs(s)

    if visited[g] == 1:
        print(f"#{i+1} 1")
    else:
        print(f"#{i+1} 0")
