def solution(id_list, report, k):
    # 중복 신고 제거
    report = list(set(report))
    
    # 신고당한 횟수 저장
    rpt_dict = {}
    for i in id_list:
        rpt_dict[i] = 0
    
    # 누가 누구를 신고했는지 저장
    rpt_by_user = {}
    for i in id_list:
        rpt_by_user[i] = []
    
    # 신고 기록 처리
    for r in report:
        a, b = r.split()   # a=신고자, b=피신고자
        
        # 피신고자 신고 횟수 증가
        rpt_dict[b] += 1
        
        # 신고자가 누구를 신고했는지 기록
        rpt_by_user[a].append(b)
    
    # 정지된 유저 목록
    stop_list = []
    for key in rpt_dict:
        if rpt_dict[key] >= k:
            stop_list.append(key)
    
    # 메일 카운트 계산
    answer = []
    for user in id_list:
        cnt = 0
        for reported in rpt_by_user[user]:
            if reported in stop_list:
                cnt += 1
        answer.append(cnt)
    
    return answer
