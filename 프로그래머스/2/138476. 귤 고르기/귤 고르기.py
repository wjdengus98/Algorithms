from collections import Counter

def solution(k, tangerine):
    counter = Counter(tangerine) #종류별 개수
    sorted_count = sorted(counter.values(), reverse = True) #개수가 많은 순으로 정렬
    
    total = 0
    result = 0
    
    for c in sorted_count:
        total += c
        result += 1
        
        if total >= k:
            break
    
    return result