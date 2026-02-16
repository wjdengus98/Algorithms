def solution(n):
    answer = []
    
    def hanoi(n, start, end, via):
        if n == 1:
            answer.append([start, end])
        else:
            hanoi(n-1, start, via, end)    # n-1개를 start→via로
            answer.append([start, end])    # 가장 큰 원판을 start→end로
            hanoi(n-1, via, end, start)    # n-1개를 via→end로
    
    hanoi(n, 1, 3, 2)
    return answer