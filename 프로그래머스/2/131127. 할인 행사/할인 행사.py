from collections import Counter

def solution(want, number, discount):
    # 1. 정현이가 원하는 제품을 딕셔너리로 정리
    want_dict = {}
    
    for i in range(len(want)):
        want_dict[want[i]] = number[i]
        
    ans = 0
    # 2. 10일 연속으로 확인(슬라이딩 윈도우 기법적용)
    for s in range(len(discount) - 9):
        # 현재 10일간의 할인 제품 카운트 (Counter 사용)
        discount_dict = Counter(discount[s:s + 10])
    
    # 3. 원하는 것과 일치하는지 확인
        if want_dict == discount_dict:
            ans += 1
            
    return ans