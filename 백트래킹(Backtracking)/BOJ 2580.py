# 백준 2580
# 스도쿠
# 백트래킹, 구현

import sys
input = sys.stdin.readline

graph = [list(map(int, input().split())) for _ in range(9)] # 스도쿠 판
    
blanks = [(i, j) for i in range(9) for j in range(9) if graph[i][j] == 0] # 비어져 있는 위치를 담을 리스트

# 행 검사
def check_row(x,n):
    for i in range(9):
        if graph[x][i] == n:
            return False
    return True

# 열 검사
def check_col(y,n):
    for i in range(9):
        if graph[i][y] == n:
            return False
    return True

# 3X3 박스 검사
def check_box(x,y,n):
    sx,sy = (x // 3) * 3, (y // 3) * 3
    
    for i in range(sx,sx + 3):
        for j in range(sy, sy + 3):
            if graph[i][j] == n:
                return False
    return True

def solve(idx=0):
    if idx == len(blanks): # 모든 빈칸 다 채웠으면
        for row in graph: # 정답 출력 후
            print(*row)
        sys.exit(0)
    
    x,y = blanks[idx] # 빈 칸 좌표
    
    for n in range(1,10): # n을 1에서 9까지 시도
        if check_box(x,y,n) and check_col(y,n) and check_row(x,n): #유효성 검사 만족하면
            graph[x][y] = n #해당 자리에 숫자 채움
            solve(idx+1) # 다음 빈칸으로 진행한다
            graph[x][y] = 0 # 실패 시 다시 빈칸으로 복원
    

solve(0)