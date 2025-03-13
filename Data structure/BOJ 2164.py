# 카드2
from collections import deque

N = int(input())

queue = deque([i for i in range(1, N+1)])


while len(queue) > 1: #카드가 한 장 남을 때까지
    queue.popleft() # 제일 위에 있는 카드 버리기
    queue.append(queue.popleft()) #그 다음 제일 위에 있는 카드를 제일 아래로 옮기기


if len(queue) == 1:
    print(queue[0]) #카드가 한 장 남았을 때 출력
