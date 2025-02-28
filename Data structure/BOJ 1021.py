# 백준 알고리즘 - 1021번 회전하는 큐
# https://www.acmicpc.net/problem/1021

from collections import deque

# 입력 받기
n, m = map(int, input().split())
nums = list(map(int, input().split()))

rotate_queue = deque([i for i in range(1, n+1)]) # 1부터 n까지의 수를 큐에 넣기

cnt = 0  # 연산 횟수

for num in nums:
    # 큐에서 num의 위치 찾기
    L = rotate_queue.index(num) # 왼쪽으로 회전하는 횟수
    R = len(rotate_queue) - L #오른쪽으로 회전하는 횟수
    
    # 왼쪽으로 회전하는 것이 더 빠른 경우
    if L <= R:
        for _ in range(L):
            rotate_queue.append(rotate_queue.popleft()) # 왼쪽 이동
        cnt += L
    # 오른쪽으로 회전하는 것이 더 빠른 경우
    else:
        for _ in range(R):
            rotate_queue.appendleft(rotate_queue.pop()) # 오른쪽 이동
        cnt += R
    
     # 맨 앞 원소 제거
    rotate_queue.popleft()
    
print(cnt)
    

