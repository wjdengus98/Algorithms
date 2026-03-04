def dfs(k, cnt, dungeons,visited):
    answer = cnt
    
    for i in range(len(dungeons)):
        min_need, fatigue = dungeons[i]
        
        # 방문하지 않거나 현재 필요도가 최소 필요 피로도보다 클 경우
        if not visited[i] and k >= min_need:
            visited[i] = True # 방문
            answer = max(answer,dfs(k - fatigue, cnt+1, dungeons,visited)) # 탐색
            visited[i] = False # 탐색한 곳 다시 초기화
    return answer

def solution(k, dungeons):
    visited = [False] * len(dungeons)     
    cnt = 0
    return dfs(k,cnt,dungeons,visited)