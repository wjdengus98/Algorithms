# 리스트에 있는 모든 곱들을 반환하는 함수
def mul(total:list) -> int:
    if len(total) == 0:
        return 0
    tot = 1
    for t in total:
        tot = tot * t
    return tot

def solution(clothes):
    dic = {}
    
    # 각 의상별로 순회하며 종류별 카운트
    for clothe in clothes:
        clothe_type = clothe[1]
        if clothe_type in dic:
            dic[clothe_type] += 1
        else:
            dic[clothe_type] = 1
    
    # 각 종류별 의상 개수에 +1 (안 입는 경우 포함)
    fashion = []
    for key in dic.keys(): 
        fashion.append(dic[key] + 1) 
    
    if len(fashion) > 1: # 의상 종류가 여러개
        return mul(fashion) - 1 # 전체 경우 - 안 입는 경우
    else: # 의상 종류 단벌
        return sum(fashion) - 1 # 전체 경우 - 안 입는 경우

