def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    for i in range(len(completion)):  # 완주자 수만큼 반복
        if participant[i] != completion[i]:
            return participant[i] #완주하지 못한 선수
    return participant[-1] #마지막 선수가 완주하지 못한 선수
    