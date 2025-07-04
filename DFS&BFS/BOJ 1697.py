# 백준 알고리즘 - 숨바꼭질
# https://www.acmicpc.net/problem/1697

from collections import deque

n,k = map(int,input().split())

visited = [-1] * 100001 # 방문 여부 및 이동 시간 기록
queue = deque() # BFS를 실행할 큐 생성

visited[n] = 0 # 시작 지점은 0초
queue.append(n) #위치를 큐에 넣고 시작

# BFS 탐색

while(queue):
    now = queue.popleft()
    if now  == k: #지금 위치가 동생의 위치이면
        print(visited[now]) #시간 출력
        break # 중단
    nxtlist = [now - 1, now + 1, now * 2] # 다음 갈 수 있는 모든 경우의 수
    for nxt in nxtlist:
        if (0 <= nxt and nxt <= 100000 and visited[nxt] == -1): #범위 및 방문 범위 설정
            visited[nxt] = visited[now] + 1 # 도달위치 = 현재 위치 + 1초
            queue.append(nxt)
        

