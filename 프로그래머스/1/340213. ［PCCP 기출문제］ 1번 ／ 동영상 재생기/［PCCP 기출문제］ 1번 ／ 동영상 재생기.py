def solution(video_len, pos, op_start, op_end, commands):
    pos_min, pos_sec = pos.split(":")
    pos_range = int(pos_min) * 60 + int(pos_sec)
    
    op_start_min, op_start_sec = op_start.split(":")
    op_start_range = int(op_start_min) * 60 + int(op_start_sec)
    
    op_end_min, op_end_sec = op_end.split(":")
    op_end_range = int(op_end_min) * 60 + int(op_end_sec)
    
    video_min, video_sec = video_len.split(":")
    video_range = int(video_min) * 60 + int(video_sec)
    
    # 오프닝 유효성 체크
    if op_start_range <= pos_range <= op_end_range:
        pos_range = op_end_range
    
    # for문 돌리기
    for command in commands:
        if command == "prev":
            if pos_range < 10:
                pos_range = 0
            else:
                pos_range -= 10 
        elif command == "next":
            rest_time = video_range - pos_range
            if rest_time < 10:
                pos_range = video_range
            else:
                pos_range += 10
        
        # 오프닝 유효성 체크
        if op_start_range <= pos_range <= op_end_range:
            pos_range = op_end_range
    
    result_min = pos_range // 60
    result_sec = pos_range % 60

    return f"{result_min:02d}:{result_sec:02d}"