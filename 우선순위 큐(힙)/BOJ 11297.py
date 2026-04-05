#  백준 최대힙

import heapq,sys
input = sys.stdin.readline

N = int(input())
hq = []

for _ in range(N):
    x = int(input())
    
    if x == 0: # x가 0이라면
        if len(hq) == 0: # 큐가 비었으면
            print(0) # 0 출력
        else: # 아니라면
            print(-heapq.heappop(hq)) # 꺼낼 때 -를 붙여 원래값 복원
    else: # x가 자연수면
        heapq.heappush(hq,-x) # 넣을 때 -붙이기 이러면 가장 큰 값에 - 때문에 - 큰 값 형태로 출력.
        