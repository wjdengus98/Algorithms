def solution(players,callings):
    # 플레이어의 이름과 등수를 저장할 딕셔너리
    rank_map = {player: idx for idx, player in enumerate(players)}
    
    for calling in callings: #부를 이름을 하나씩 확인
        current_rank = rank_map[calling] # 현재 등수 출력
        
        if current_rank == 0: # 1등이면 건너뜀
            continue
        
        # 앞서고 있는 플레이어의 이름 확인
        front_player = players[current_rank - 1]
        
        # 추월할 경우 서로 바꿈
        players[current_rank - 1], players[current_rank] = players[current_rank], players[current_rank - 1]
        
        rank_map[calling] -= 1 # 등수 상승
        rank_map[front_player] += 1 #등수 하강
               
    return players