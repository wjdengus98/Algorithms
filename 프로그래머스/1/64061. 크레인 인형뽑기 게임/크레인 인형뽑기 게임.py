def solution(board, moves):
    stack = []
    cnt = 0
    
    for i in moves:
        for j in range(len(board)):
            doll = board[j][i - 1]
            if doll != 0:
                stack.append(doll)
                board[j][i - 1] = 0
                break
        if len(stack) > 1:
            if stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
                cnt += 2
    return cnt