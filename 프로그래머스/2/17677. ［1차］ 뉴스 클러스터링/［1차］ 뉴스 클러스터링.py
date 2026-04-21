from collections import Counter

def solution(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()

    lst1 = []
    lst2 = []

    for i in range(len(str1) - 1):
        chunk = str1[i:i+2]

        if chunk.isalpha():
            lst1.append(chunk)

    for j in range(len(str2) - 1):
        chunk = str2[j:j+2]

        if chunk.isalpha():
            lst2.append(chunk)

    c1 = Counter(lst1)
    c2 = Counter(lst2)
    
    gyojiphap = list((c1 & c2).elements()) # 교집합 요소 추출
    hapjiphap = list((c1 | c2).elements()) # 합집합 요소 추출

    # 집합 A와 B가 모두 공집합ㄹ 일경우 자카드 유사도 1, 최종결과:65536
    if len(gyojiphap) == 0 and len(hapjiphap) == 0:
        return 65536
    else:
        Jaccard = (len(gyojiphap) / len(hapjiphap)) * 65536
    
    result = int(Jaccard)
    return result