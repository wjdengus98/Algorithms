#  백준 최소힙

import heapq,sys
input = sys.stdin.readline
hq = []

N = int(input())

for _ in range(N):
    x = int(input())
    
    if x == 0: #만약 x가 0이면 가장 작은 값 출력
        if len(hq) == 0: # 우선순위 큐 비어져있을경우
            print(0) # 0 출력
        else: # 작은 값 출력 후 제거
            print(heapq.heappop(hq))
    else: # 만약 x가 0이 아니고 자연수라면
        heapq.heappush(hq,x)