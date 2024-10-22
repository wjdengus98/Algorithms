#백준 9372(상근이의 여행)

#DFS 이용

#기본 아이디어:
#1. DFS로 국가를 방문하면서, 새로운 국가로 이동할 때마다 간선의 개수를 1씩 증가시킵니다.
#2. 연결된 그래프에서 모든 국가를 한 번씩 방문하고, 마지막에 방문한 간선의 개수를 리턴합니다.

def dfs(country, visited, node):
    
    visited[node] = True
    cnt = 0
    for i in country[node]:
        if not visited[i]:
            cnt += 1
            cnt += dfs(country, visited, i)
    return cnt


T = int(input())



for _ in range(T):
    n,m = map(int,input().split())
    country = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b = map(int,input().split())
        
        country[a].append(b)
        country[b].append(a)

    visited = [False] * (n+1)
    count = dfs(country, visited, 1)
    print(count)