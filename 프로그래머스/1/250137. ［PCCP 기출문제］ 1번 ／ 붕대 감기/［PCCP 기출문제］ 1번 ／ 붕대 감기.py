def solution(bandage, health, attacks):
    max_time = attacks[len(attacks) - 1][0] # 11
    HP = health # 30
    attk_times = [attacks[i][0] for i in range(len(attacks))] 
    damages = [attacks[i][1] for i in range(len(attacks))] 
    sequence = 0
    
    for i in range(max_time + 1):
        cur_time = i
        
        if cur_time == attk_times[0]: #공격 턴
            HP -= damages[0]
            sequence = 0
            attk_times.pop(0)
            damages.pop(0)
            
            if HP <= 0:
                return -1
        else: # 붕대 턴
            HP += bandage[1]
            sequence += 1
            
            if sequence == bandage[0]: # 연속 공격 성공 시
                HP += bandage[2] # 추가 체력 회복
                sequence = 0 # 연속 공격 초기화
            
            if HP > health:
                HP = health   
    return HP