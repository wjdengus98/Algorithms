def solution(n,words):
    seen = set() #중복단어 방지하기 위한 튜플
    
    for i in range(len(words)):
        current = words[i] #현재 단어
        
        if current in seen: #중복 단어 리스트에 있으면
            #탈락
            number = (i % n) + 1
            sequence = (i // n) + 1
            return [number, sequence]

        
        if i > 0 and words[i-1][-1] != current[0]: #현재 단어 첫글자 이전 단어 마지막 글자 다르면 끝말잇기 X
            #탈락
            number = (i % n) + 1
            sequence = (i // n) + 1
            return [number, sequence]
        
           
        seen.add(current)
        
    return [0,0]