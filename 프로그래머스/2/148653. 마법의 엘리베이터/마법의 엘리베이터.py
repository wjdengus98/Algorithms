def solution(storey):
    
    result = 0
    
    while storey > 0:
        
        number = storey % 10 # 일의 자리
        
        if number > 5: # 일의 자리가 5,6,7,8인 경우 올림
            result += (10 - number)
            storey += 10 # 십의 자리 올림 반영
        
        elif number == 5: # 일의 자리가 5일 때
            next_num = (storey // 10) % 10 # 다음 자릿수
            
            if next_num >= 5: # 다음 자릿수가 5 이상이면 올림
                result += number 
                storey += 10
            else: # 다음 자릿수가 5 이하면 내림
                result += number
        else: # 일의 자리가 5 이하인 경우 내림
            result += number
        
        storey = storey // 10
    
    return result