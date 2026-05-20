# 재귀를 돌린다.=> 시간 초과 너무 많이남
# 시간복잡도 3^1,000,000 => 시간 초과
# bfs문으로 탐색할 경우, 시간 복잡도 O(y)

from collections import deque

def solution(x, y, n):
    if x == y:
        return 0
    
    visited = set()
    queue = deque([(x,0)])
    
    while queue:
        cur,cnt = queue.popleft()
        
        for next_val in [cur * 2, cur + n, cur *3]:
            if next_val == y:
                return cnt+1
            elif next_val < y and next_val not in visited:
                visited.add(next_val)
                queue.append((next_val, cnt + 1))
    return -1