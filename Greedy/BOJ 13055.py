# 백준 주유소
# 그리디 알고리즘
n = int(input()) #도시의 개수

dist = list(map(int, input().split())) # 도시를 연결하는 도로의 길이
prices = list(map(int, input().split())) #L당 기름의 가격
 
nowP = prices[0] #첫번째 도시의 기름 가격
total = 0 #총 비용
nowD = dist[0] #첫번째 도시의 거리

for i in range(1, n - 1):
    if prices[i] < nowP: #현재 도시의 기름 가격이 더 싸면
        total += nowP * nowD #현재 도시까지의 기름 가격을 더한다
        nowP = prices[i] #기름 가격을 갱신
        nowD = dist[i] #거리를 갱신
    else: #현재 도시의 기름 가격이 더 비싸면
        nowD += dist[i] #거리를 더한다
       

total += nowP * nowD #마지막 도시까지의 기름 가격을 더한다
print(total) #총 비용 출력
