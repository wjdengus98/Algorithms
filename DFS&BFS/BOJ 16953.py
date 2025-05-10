# 백준 알고리즘
# A → B
# https://www.acmicpc.net/problem/16953
# visited을 배열로 쓸 경우 메모리 초과 발생 -> set으로 변경

import sys
from collections import deque

input = sys.stdin.readline
A, B = map(int,input().split())
visited = set() #방문한 숫자 저장
queue = deque() # 큐 생성
visited.add(A) # A를 방문한 숫자로 추가

queue.append((A, 1)) # 큐에 A와 카운트 1을 추가
# BFS
while queue:
    n, cnt = queue.popleft() # n은 현재 값, cnt는 카운트
    if n == B:  # n이 B와 같으면
        print(cnt) # 카운트 출력
        break
   
    next1 = n * 2 # n을 2배로 늘린 값
    if next1 <= B and next1 not in visited: # n을 2배로 늘린 값이 B보다 작고 방문하지 않았다면
        visited.add(next1)
        queue.append((next1, cnt + 1)) # 큐에 추가
    
    next2 = n * 10 + 1 # n을 10배로 늘리고 1을 더한 값
    if next2 <= B and next2 not in visited: # n을 10배로 늘리고 1을 더한 값이 B보다 작고 방문하지 않았다면
        visited.add(next2)
        queue.append((next2, cnt + 1)) # 큐에 추가
else:
    print(-1)
    


