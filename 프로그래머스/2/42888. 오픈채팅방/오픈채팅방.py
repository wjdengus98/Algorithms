def solution(record):
    ans = []
    info_dict = {}
    
    for info in record:
        cmd = info.split(" ")
        
        if cmd[0] in ['Enter', 'Change']: # Enter or Change인 경우
            info_dict[cmd[1]] = cmd[2]
            
    for info in record:
        cmd = info.split(" ")
        
        if cmd[0] == "Enter":
            ans.append(f"{info_dict[cmd[1]]}님이 들어왔습니다.")
        elif cmd[0] == "Change":
            pass
        else:
            ans.append(f"{info_dict[cmd[1]]}님이 나갔습니다.")
    return ans