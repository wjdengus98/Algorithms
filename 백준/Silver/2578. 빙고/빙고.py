# 백준 알고리즘 - 2578번
# 빙고
# https://www.acmicpc.net/problem/2578


bingo = [list(map(int, input().split())) for _ in range(5)] # 빙고판 입력 받기
speak = [] # 불러온 숫자 입력 받기
for _ in range(5): 
    speak += list(map(int, input().split())) # 불러온 숫자 입력

def check(board):
    bingo_count = 0 # 빙고 만든 개수
    
    #가로 탐색하기
    for row in board:
        if row.count(0) == 5:
            bingo_count += 1
            
    #세로 탐색하기
    for col in range(5):
        if [board[row][col] for row in range(5)].count(0) == 5:
            bingo_count += 1
    
    #대각선 탐색하기
    
    #1. (0,0), (1,1), (2,2), (3,3), (4,4) 부분 탐색
    if [board[i][i] for i in range(5)].count(0) == 5:
        bingo_count += 1
    #2. (0,4), (1,3),(2,2),(3,1),(4,0) 부분 탐색
    if [board[i][4-i] for i in range(5)].count(0) == 5:
        bingo_count += 1
    
    return bingo_count
    


for i in range(25):
    for j in range(5):
        for k in range(5):
            if speak[i] == bingo[j][k]: # 불러온 숫자와 빙고판의 숫자가 일치하면
                bingo[j][k] = 0 # 해당 위치를 0으로 변경
        
    if check(bingo) >= 3: # 빙고가 3개 이상 만들어졌다면
        print(i + 1)# 몇 번째 숫자를 부른 후 빙고가 3개 이상 만들어졌는지 출력
        break
                
