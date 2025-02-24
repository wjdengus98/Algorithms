#백준 알고리즘 - 1012번
# https://www.acmicpc.net/problem/1012

import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 증가

def dfs(x, y, n, m, board):
    if x < 0 or x >= n or y < 0 or y >= m:  # 올바른 인덱스 범위 확인
        return False
    if board[x][y] == 1:  # 배추가 있다면
        board[x][y] = 0  # 방문 처리
        # 상, 하, 좌, 우 탐색
        dfs(x-1, y, n, m, board)
        dfs(x+1, y, n, m, board)
        dfs(x, y-1, n, m, board)
        dfs(x, y+1, n, m, board)
        return True
    return False

t = int(input())  # 테스트 케이스 개수

for _ in range(t):
    m, n, k = map(int, input().split())  # 가로(m), 세로(n), 배추 개수
    board = [[0] * m for _ in range(n)]  # 주어진 크기로 보드 초기화

    for _ in range(k):  # 배추 심어진 위치 입력받기
        x, y = map(int, input().split())
        board[y][x] = 1  # 좌표 저장 (x, y는 가로, 세로 좌표지만 2차원 배열에서는 y, x로 저장해야 함)

    result = 0  # 필요한 지렁이 수

    for i in range(n):  # 세로 (행)
        for j in range(m):  # 가로 (열)
            if dfs(i, j, n, m, board):  # 배추 군집 발견 시
                result += 1

    print(result)  # 결과 출력
