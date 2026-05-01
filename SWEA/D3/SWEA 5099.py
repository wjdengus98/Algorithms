# [S/W 문제해결 기본] 6일차 - 피자 굽기

from collections import deque

T = int(input())

for i in range(T):
    N,M = map(int,input().split()) # 화덕의 크기 N, 피자 개수 M
    cheese = list(map(int,input().split()))
    q = deque()

    for j in range(N):
        q.append((j+1,cheese[j]))

    next_pizza = N

    while len(q) > 1:
        num,c = q.popleft() #1번 자리에서 꺼내기
        c = c // 2

        if c == 0:
            # 새 피자 추가
            if next_pizza < M: #대기 피자가 있는 경우만
                q.append((next_pizza + 1, cheese[next_pizza]))
                next_pizza += 1
        else: # 치즈가 0이 아니면
            q.append((num,c))

    print(f"#{i+1} {q[0][0]}")