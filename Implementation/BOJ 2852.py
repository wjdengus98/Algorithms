# 백준 2852번
# NBA 농구
# 구현, 누적합

def to_second(t): #문자열 (MM:SS)를 초 단위로 변경해주는 함수
    min,sec = t.split(":")
    total = int(min) * 60 + int(sec)
    return total

def format_time(t): #초 단위 함수를 다시 (MM:SS)로 변경해주는 함수
    min = t // 60
    sec = t % 60
    return f"{min:02}:{sec:02}"
    

N = int(input())
records = []

# 각 팀 번호와 득점 시간 형태로 저장
for _ in range(N):
    team, t = input().split()
    records.append((int(team),to_second(t)))

score1, score2 = 0,0 #팀 별 점수
time1, time2 = 0,0 #팀 별 시간
prev = 0 #직전 득점 시간

for team,cur in records:

    diff = cur - prev #직전 득점 시간과 현재 시간 차이
    
    if score1 > score2: #점수가 더 높으면 시간차를 각 팀별로 더한다
        time1 += diff
    elif score2 > score1:
        time2 += diff
        
    #점수 갱신하기
    if team == 1:
        score1 += 1
    else:
        score2 += 1
    
    prev = cur #이전 시간 갱신하기 

final = 2880 # 농구 48분(마지막 시간)
diff = final - prev #마지막 시간과 이전 시간 차이

if score1 > score2:# 점수가 더 높으면 마지막 시간 차를 각 팀별로 더한다
    time1 += diff
elif score2 > score1:
    time2 += diff

# 결과 출력하기
print(format_time(time1)) 
print(format_time(time2))


    
    
        
        
