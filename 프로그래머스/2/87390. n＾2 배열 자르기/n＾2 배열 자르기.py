'''아이디어
행과 열의 인덱스
arr[0][0] => 행,열  =(0 + 1) = 1
arr[0][1], arr[1][0], arr[1][1] => 행과 열 중 큰 숫자에다가 +1을 더하는 게 관련 숫자가 들어간다.
'''

def solution(n, left, right):
    answer = []
    
    for i in range(left, right+1): #left에서 right 까지
        row = i // n # 1차원 배열의 행을 2차원으로 변환
        col = i % n # 1차원 배열의 열을 2차원으로 변환
        
        answer.append(max(row,col) + 1) # 아이디어 적용
    return answer