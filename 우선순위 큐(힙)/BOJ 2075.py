#백준 N번째 큰 수

# n = int(input())

# grid = []

# for i in range(n):
#     grid.append(list(map(int, input().split())))
    
# all = []

# for i in range(n):
#     for g in grid[i]:
#         all.append(g)
        
# all.sort(reverse=True)

# print(all[n-1])

# 이와 같은 코드의 경우 18MB로 메모리 초과가 발생한다
# 리스트를 2개를 사용하므로 메모리 초과가 발생
# 이를 해결하기 위해 heapq를 사용한다.

import heapq
import sys

input = sys.stdin.readline

n = int(input())

top_n = []

for _ in range(n):
    numbers = list(map(int, input().split()))
    for num in numbers:
        if len(top_n) < n:
            heapq.heappush(top_n, num) # 힙의 크기가 N보다 작으면 그냥 추가
        else:
            heapq.heappushpop(top_n, num)  # 가장 작은 값 제거하고 새로운 값 추가

print(top_n[0])