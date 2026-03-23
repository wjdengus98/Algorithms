# 백준 
# 카드1

from collections import deque

N = int(input())

dq = deque(range(1,N+1))
rest = []

while len(dq) != 1:
    throw = dq.popleft()
    rest.append(throw)
    
    dq.append(dq.popleft())

rest.append(dq[0])
print(*rest)
