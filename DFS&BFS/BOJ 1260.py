#백준 DFS와 BFS(1260)

def dfs(c):
    ans_dfs.append(c) #방문 노드 추가
    visited[c] = True #방문 표시

    for n in adj[c]:
        if not visited[n]: #방문하지 않았다면
            dfs(n) #방문

def bfs(s):
    q = [] #필요한 q,v[] 변수 배열 생성
    q.append(s) #q에 초기데이터 삽입
    ans_bfs.append(s)
    visited[s] = True

    while q:
        c = q.pop(0)
        for n in adj[c]:
            if not visited[n]: #방문하지 않은 노드는 q에 삽입
                q.append(n)
                ans_bfs.append(n)
                visited[n] = True


n,m,v = map(int,input().split())
adj = [[] for _ in range(n+1)]
for _ in range(m):
    s,e = map(int,input().split())
    adj[s].append(e)
    adj[e].append(s) #양방향

#[1] 오름차순 정렬
for i in range(1,n+1):
    adj[i].sort()


visited = [0] * (n+1)
ans_dfs = []
dfs(v)

visited = [0] * (n+1)
ans_bfs = []
bfs(v)

print(*ans_dfs)
print(*ans_bfs)
