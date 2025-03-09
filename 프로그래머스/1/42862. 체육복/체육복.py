def solution(n, lost, reserve):
    set_reserve = set(reserve) - set(lost) #여벌 학생복을 가진 학생 중 도난 x
    set_lost = set(lost) - set(reserve) #도난 당한 학생 중 여벌 체육복 x
    
    for i in set_reserve: #여벌 학생복을 가진 학생 중에서
        if i-1 in set_lost: #앞 학생이 도난 당하고 여벌 체육복 X
            set_lost.remove(i - 1) #빌려준다
        elif i + 1 in set_lost: # 뒤 학생이 도난당하고 여벌 체육복 X
            set_lost.remove(i + 1) #빌려준다
                
    return n - len(set_lost)