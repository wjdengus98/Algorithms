def solution(today, terms, privacies):
    # 1. 정수형으로 바꿔보기
    today = int(today[:4]) * 12 * 28 + int(today[5:7]) * 28 + int(today[8:])
    # 2. terms 딕셔너리 변환 후 privacies 순환하기
    term_dict = {} #딕셔너리 선언
    res = [] #결과 담을 리스트 선언
    
    for term in terms: 
        key = term[0] # 약관 종류
        val = term[2:] # 유효 기관
        term_dict[key] = int(val) # 딕셔너리 생성
    
    for i in range(len(privacies)):
        privacy = privacies[i]
        
        date, rank = privacy.split() #개인정보 수집 일자, 약관 종류
        
        if rank in term_dict:
            d =  int(date[:4]) * 12 * 28 + int(date[5:7]) * 28 + int(date[8:]) # 정수 변환
            expire = d + term_dict[rank] * 28 #만료 날짜
            
            if expire <= today: #만료날짜가 오늘 날짜보다 작거나 같으면
                res.append(i+1) #파기
    
    return res