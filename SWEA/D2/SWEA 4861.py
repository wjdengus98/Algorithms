# 삼성 SW ACADEMY
# 4861. [S/W 문제해결 기본] 3일차 - 회문

t = int(input())

for tc in range(t):
    board = []
    N,M = map(int,input().split())
    
    for j in range(N):
        chunk = list(input())
        board.append(chunk)
    
    palindromes = []
    
    # 가로에서 회문 찾는 법
    for i in range(N):
        for j in range(N - M + 1): 
            word = ""
            for k in range(M):
                word += board[i][j + k]
            if word == word[::-1]:
                palindromes.append(word)
    
    # 세로에서 회문 찾는 법
    for j in range(N):      
        for i in range(N - M + 1):  
            word = ""
            for k in range(M):
                word += board[i + k][j]  
            if word == word[::-1]:
                palindromes.append(word)
    
    print(f"#{tc+1} {palindromes[0]}")  

    
