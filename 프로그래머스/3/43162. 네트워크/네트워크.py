def dfs(computers, visited, start, n):
    for j in range(n):
        if computers[start][j] and not visited[j]:
            visited[j] = True
            dfs(computers,visited,j,n)


def solution(n, computers):
    visited = [0] * n
    cnt = 0
    
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            dfs(computers, visited,i,n)
            cnt += 1
    
    return cnt