#백준 올림픽(8979번)
n,k = map(int,input().split())

countries = [] #각 나라 리스트

# 각 나라의 정보를 저장 (나라 번호, 금, 은, 동 메달 수)
for _ in range(n):
    countries.append(list(map(int,input().split())))
    

# k번째 나라의 메달 정보를 가져옴
target_country = []
for country in countries:
    if country[0] == k:
        target_country = country
        break


# k 번째 나라의 순위 계산    
rank = 1
for country in countries:
        if k != country[0]:
            if country[1] > target_country[1]: #금메달 수가 더 많은 나라 비교
                rank += 1
            if country[1] == target_country[1] and country[2] > target_country[2]: #금메달 수는 같고 은메달 수가 더 많은 나라 비교
                rank += 1
            if country[1] == target_country[1] and country[2] == target_country[2] and country[3] > target_country[3]: # 금,은 메달 수는 같고 동메달 수가 더 많은 나라 비교
                rank += 1
    
print(rank)