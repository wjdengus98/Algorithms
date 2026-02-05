def solution(citations):
    citations.sort(reverse=True) 
    h = 0
    
    for i in range(len(citations)):
        # i+1편의 논문을 봤을 때, 그 논문들이 최소 몇 회 인용되었나?
        if citations[i] >= i + 1:
            h = i + 1
        else:
            break
    
    return h