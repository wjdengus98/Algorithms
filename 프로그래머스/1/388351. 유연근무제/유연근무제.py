def to_minutes(hhmm):
    hour = hhmm // 100
    minute = hhmm % 100
    return hour * 60 + minute

def solution(schedules, timelogs, startday):
    res = 0

    for i in range(len(schedules)):
        commute = to_minutes(schedules[i])  # 출근 희망 시각을 분으로 변환
        cnt = 0
        day = startday

        for j in range(len(timelogs[i])):
            if day in [6, 7]:  # 주말은 이벤트 제외
                day = (day % 7) + 1
                continue

            log_time = to_minutes(timelogs[i][j])  # 실제 출근 시각도 분으로 변환
            if log_time <= commute + 10:
                cnt += 1

            day = (day % 7) + 1

        if cnt == 5:
            res += 1

    return res
