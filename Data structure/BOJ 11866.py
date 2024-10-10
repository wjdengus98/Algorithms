#요세푸스 순열
from collections import deque

n, k = map(int,input().split())

dq = deque(range(1, n+1))
queue = []
    

while dq:
    for i in range(k-1): #k-1번 회전
        dq.append(dq.popleft()) #맨 앞의 요소를 뒤로 보냄
    queue.append(dq.popleft()) #k번째 요소를 결과에 추가

print("<", end="")
print(", ".join(map(str,queue)), end="")
print(">")