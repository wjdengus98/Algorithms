# 백준 알고리즘
# 킹(1063번)

board = [[0] * 8 for _ in range(8)]

direction = {
    'R':  (1, 0),
    'L':  (-1, 0),
    'T':  (0, 1),
    'B':  (0, -1),
    'RT': (1, 1),
    'RB': (1, -1),
    'LT': (-1, 1),
    'LB': (-1, -1),
}

k, s, n = map(str,input().split())

x1 = ord(k[0]) - ord('A')
y1 = int(k[1]) - 1

x2 = ord(s[0]) - ord('A') 
y2 = int(s[1]) - 1

board[x1][y1] = 1
board[x2][y2] = 2

for i in range(int(n)):
    loc = input().strip()
    dx,dy = direction[loc]
    
    nx1,ny1 = x1 + dx, y1 + dy
    
    if nx1 < 0 or nx1 > 7 or ny1 < 0 or ny1 > 7:
        continue  # 범위 밖이면 이동 무시
    
    if board[nx1][ny1] == 2:
        nx2,ny2 = x2 + dx, y2 + dy
        
        if nx2 < 0 or nx2 > 7 or ny2 < 0 or ny2 > 7:
            continue  # 범위 밖이면 이동 무시
        
        # 돌 이동 확정
        board[x2][y2] = 0
        board[nx2][ny2] = 2
        x2, y2 = nx2, ny2
    
     # 킹 이동 확정
    board[x1][y1] = 0
    board[nx1][ny1] = 1
    x1, y1 = nx1, ny1
    
print(chr(x1 + ord('A')) + str(y1 + 1))  
print(chr(x2 + ord('A')) + str(y2 + 1)) 