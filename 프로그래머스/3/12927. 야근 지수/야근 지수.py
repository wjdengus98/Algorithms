import heapq

def solution(n, works):
    heap = [-w for w in works] # 음수로 변환
    heapq.heapify(heap) # 힙으로 변환
    
    while n > 0:
        max_num = heapq.heappop(heap)
        if max_num == 0:
            break
        heapq.heappush(heap, max_num + 1) # 음수라서 +1이 1 감소
        n -= 1
    
    origin_heap = [(-h)**2 for h in heap]
    result = sum(origin_heap)
    return result