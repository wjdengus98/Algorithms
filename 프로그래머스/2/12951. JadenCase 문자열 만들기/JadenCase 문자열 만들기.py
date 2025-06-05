def solution(s):
    res = ""
    flag = True #단어의 첫 글자인지 여부
    
    for ch in s:
        if ch == " ": # 공백이면 그대로 더한다
            res += ch
            flag = True
        else: # 공백이 아니고 단어
            if flag: # 첫 글자
                res += ch.upper() #대문자변환 
                flag = False # 나머지는 False
            else:
                res += ch.lower()
    
    return res