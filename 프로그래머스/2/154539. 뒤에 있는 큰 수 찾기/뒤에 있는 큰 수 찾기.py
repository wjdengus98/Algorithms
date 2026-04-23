# 뒤에 있는 큰 수 찾기

def solution(numbers):
    stack = [] #인덱스 집어넣기 
    result = [-1] * len(numbers) # -1로 배열 채움
    
    for i in range(len(numbers)):
        # 스택이 비지 않고, 이후값이 전의 값보다 크면
        while stack and numbers[stack[-1]] < numbers[i]:
            idx = stack.pop() #스택에 저장된 인덱스 출력
            result[idx] = numbers[i] #result 인덱스를 이후값으로 변경
        stack.append(i) 
    return result
