# SWEA 파이썬 S/W 문제해결 기본 2일치 - 색칠하기

T = int(input()) # 테스트 케이스

for i in range(T):
    board = [[0] * 10 for _ in range(10)] # 10 X 10 종이판
    n = int(input())
    
    for j in range(n):
        r1,c1,r2,c2,color = map(int,input().split()) #각 점들의 좌표 및 색깔
        
        # 각 좌표를 순회하며 지정된 색깔로 칠하기
        for r in range(r1, r2 + 1): 
            for c in range(c1, c2 + 1):
                board[r][c] += color # 핵심!계속 칠하면 색깔이 더해진다! 
    cnt = 0 # 특정한 색깔을 세는 변수 cnt
    for r in range(10):
        for c in range(10):
            # 모든 점들을 순회하며
            if board[r][c] == 3: # 색깔이 보라색일때 빨강 = 1, 파란 = 2 섞임. 
                cnt += 1 # 겹치는 수를 센다.
    
    print(f"#{i + 1} {cnt}")    

        