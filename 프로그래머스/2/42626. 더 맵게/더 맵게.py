import heapq

def solution(scoville, K):
    heapq.heapify(scoville)  # 최소 힙으로 변환
    count = 0
    
    while len(scoville) > 1:
        if scoville[0] >= K:
            return count
        
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        
        new_food = first + (second * 2)
        heapq.heappush(scoville, new_food)
        
        count += 1
    
    # 마지막 음식 체크
    if scoville[0] >= K:
        return count
    else:
        return -1