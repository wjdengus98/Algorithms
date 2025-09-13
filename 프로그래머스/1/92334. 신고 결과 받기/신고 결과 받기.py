def solution(id_list, report, k):
    report = list(set(report))
    
    #신고 당한 횟수 저장
    rpt_dict = {}
    for i in id_list:
        rpt_dict[i] = 0
    
    #다른 유저가 신고한 횟수 저장
    rpt_by_user = {}
    for i in id_list:
        rpt_by_user[i] = []
    
    #신고 처리
    for r in report:
        a,b = r.split()
        
        #피신고자 횟수 증가
        
        if b not in rpt_dict:
            rpt_dict[b] = 1
        else:
            rpt_dict[b] += 1
        
        #신고자가 누굴 신고했는지 기록
        rpt_by_user[a].append(b)
    
    
    #정지된 목록 추가
    stop_list = []
    for key in rpt_dict:
        id_cnt = rpt_dict[key]
        if id_cnt == k:
            stop_list.append(key)
    
    #매일 카운트 계산하기
    answer = []
    for user in id_list:
        cnt = 0
        for reported in rpt_by_user[user]:
            if reported in stop_list:
                cnt += 1
        answer.append(cnt)
    
    return answer