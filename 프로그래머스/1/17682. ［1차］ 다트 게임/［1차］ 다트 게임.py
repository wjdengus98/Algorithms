def solution(dartResult):
    scores = [] #다트에서 얻은 점수를 저장할 리스트
    idx = 0 # 인덱스
    power = {'S' : 1, 'D' : 2, "T": 3} #SDT에 대한 각각 점수 리스트
    
    for i in range(len(dartResult)):
        op = dartResult[i] # OP를 선택
        if op in power: #'S', 'D', 'T' 연산자면 
            scores.append(int(dartResult[idx:i]) ** power[op]) #리스트에 넣기
        elif op == "*": # 스타상이면
            scores[-2:] = [x * 2 for x in scores[-2:]] #마지막 2개 고른 뒤 2배
        elif op == "#": # 아차상이면 부호 반대 
            scores[-1] = -scores[-1]
        
        if not op.isnumeric(): #OP가 연산자가 아니면
            idx = i + 1 #인덱스 증가
            
    return sum(scores) #다트 점수의 총합 출력