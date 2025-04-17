def solution(s):
    count = 0  # 잘라낸 문자열의 개수
    i = 0  # 현재 탐색 시작 위치
    
    while i < len(s):
        x = s[i]
        x_count = 1
        not_x_count = 0
        i += 1
        
        while i < len(s):
            if s[i] == x:
                x_count += 1
            else:
                not_x_count += 1
            i += 1
            
            if x_count == not_x_count:
                break
        
        count += 1
    
    return count
