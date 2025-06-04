def solution(s, skip, index):
    answer = ""
    for i in range(len(s)):
        ASC = ord(s[i])
        alpha = []
        
        while (len(alpha) != index):
            ASC += 1
            if ASC > 122:
                ASC = 97
            char = chr(ASC)
            
            if char not in skip:
                alpha.append(char)
            else:
                continue
        answer += alpha[-1]
    return answer