# 1215. [S/W 문제해결 기본] 3일차 - 회문1

def find_palindrome(n,board):
    cnt = 0
    
    # 회문 가로 탐색
    for i in range(8):
        for j in range(8-n+1):
            row_word = board[i][j:j+n]

            if row_word == row_word[::-1]:
                cnt += 1
    
    # 회문 세로 탐색:
    for i in range(8-n+1):
        for j in range(8):
            col_word=''
            
            for k in range(n):
                col_word += board[i+k][j]
                
            if col_word == col_word[::-1]:
                cnt += 1
    return cnt
                

for tc in range(10):
    n = int(input())
    board = []
    
    for i in range(8):
        letters = input()
        board.append(letters)
    
    answer = find_palindrome(n,board)
    print(f"#{tc+1} {answer}")
    
    