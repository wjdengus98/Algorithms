import heapq

def solution(operations):
    heap = []

    for i in range(len(operations)):
        op, val = operations[i].split(" ")

        if op == "I": # 큐에 삽입
            heapq.heappush(heap,int(val))
        elif op == "D" and val == "1":
            if heap: #최대값 제거 -> 리스트에서 최대값 삭제
                heap.remove(max(heap))
        else: #최소값 제거 -> 우선순위 큐 삭제
            if heap:
                heapq.heappop(heap)

    if len(heap) == 0:
        return [0,0]
    else:
        return [max(heap),min(heap)]