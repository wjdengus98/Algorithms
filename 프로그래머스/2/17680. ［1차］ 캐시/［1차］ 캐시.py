from collections import deque

def solution(cacheSize, cities):
    # cacheSize=0 이면 캐시가 없으니 항상 miss
    if cacheSize == 0:
         return len(cities) * 5

    cache = deque()
    answer = 0
    
    for city in cities:
        city = city.lower() # 도시 이름 통일
        
        if city in cache: #city가 이미 캐쉬 메모리상에 있다면 => 이 경우 캐시 hit
            cache.remove(city) #기존 위치에서 도시 제거 
            cache.append(city) # 맨 뒤로 도시 이동
            answer += 1
        else: #city가 캐쉬 메모리상에 없다면 => 이 경우 캐시미스
            if len(cache) >= cacheSize: #꽉 찼으면
                cache.popleft() # 가장 오래된 거 삭제
            cache.append(city)
            answer += 5
    return answer