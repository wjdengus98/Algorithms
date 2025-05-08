def solution(ingredient):
    hamburger = [1,2,3,1] #햄버거 배열
    count = 0 #햄버거 개수
    stack = [] # 스택 생성
    
    for i in ingredient:
        stack.append(i) #재료를 스택에 담고
        
        if stack[-4:] == hamburger: #마지막 4개가 햄버거 구성 일치 확인
            count += 1 #일치하면 증가
            
            for _ in range(4):
                stack.pop() #햄버거 포장(삭제)
            
    return count #개수 반환