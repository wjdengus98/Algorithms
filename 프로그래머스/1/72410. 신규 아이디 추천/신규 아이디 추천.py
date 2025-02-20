def solution(new_id):
    answer = ''
    new_id = new_id.lower() # 1. 대문자 -> 소문자
    
    for i in new_id: # 2. 소문자, 숫자, -, _, . 제외한 문자 제거
        if i.islower() or i.isdigit() or i in ['-', '_', '.']:
            answer += i
            
    while ".." in answer: # 마침표 2번 이상 연속 -> 하나로 치환환
        answer = answer.replace("..", ".")
        
    if answer[0] == '.' or answer[-1] == '.': #처음,끝에 위치한 '.' 제거
        answer = answer.strip('.')
        
    if answer == '': #빈 문자일 시 'a' 추가
        answer ='a'
        
    if len(answer) >= 16: # 16자 이상이면 15자로 제한
        answer = answer[:15]
        if answer[-1] == '.': # 마지막 문자가 '.'일 시 제거
            answer = answer[:-1]
            
    while len(answer) <= 2: # 2자 이하 -> 마지막 문자를 3자 될 때까지 반복
        answer += answer[-1]
    
    return answer