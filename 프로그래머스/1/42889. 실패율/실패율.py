def solution(N, stages):
    f_list = [] #실패율 담을 리스트
    total = len(stages)
    
    for i in range(1, N+1): 
        count = stages.count(i) # stage의 자연수를 셈
        if total == 0: #스테이지에 자연수가 없으면
            rate = 0 #실패율은 0
        else:
            rate = count / total #실패율 
            total -= count # 실패율에서 클리어한 넘버 제거 
        f_list.append((i, rate))
    
    f_list.sort(key = lambda x :-x[1]) #key로 실패율 내림차순 정렬
    
    return [x[0] for x in f_list] # 스테이지의 번호만 출력
    