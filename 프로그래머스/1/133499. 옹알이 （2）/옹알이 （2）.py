def solution(babbling):
    can_speak = ["aya", "ye", "woo", "ma"]
    answer = 0
    for babble in babbling:
        word = babble
        prev = "" # 이전 발음 기록
        flag = True # 단어 성공 여부
        
        while word and flag:
            found = False
            
            for sound in can_speak:
                if word.startswith(sound) and sound != prev: # sound가 Babbling 안에 있고,연속해서 같은 발음을 하는 것을 막기.
                    word = word[len(sound):] # 해당 단어 제거
                    prev = sound
                    found = True
                    break
            if not found: #  sound가 word에 포함안되어 있으면
                flag = False #단어 발음 불가
        
        if flag and not word: #단어 발음 가능, word가 다 제거되었으면
            answer += 1 #카운트
            
    return answer