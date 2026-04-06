# 백준 절댓값 힙

import heapq,sys

input = sys.stdin.readline

N = int(input())

hq = []

for _ in range(N):
    x = int(input())
    
    if x != 0: # x가 0이 아니면
        heapq.heappush(hq, (abs(x),x)) # 힙에 (절댓값, 원래값) 삽입
    else: # x가 0이면
        if len(hq) == 0: # 힙이 비었을 때
            print(0) # 0출력
        else: # 힙이 비지 않았을 때
            print(heapq.heappop(hq)[1]) # hq = [(1,-1), (1,1)] 이 중 (1,-1)의 1번 인덱스(원래값) 출력