# 백준 알고리즘 - 15652번
# https://www.acmicpc.net/problem/15652

arr = []

def recur(count):
    if count == M:
        print(*arr)
        return
    
    for i in range(1, N+1):
        if arr and arr[-1] > i: # 이전 원소가 현재 원소보다 크면 continue ex) [2,1] -> 스킵할 수 있음
            continue
        arr.append(i)
        recur(count+1)
        arr.pop()
        

N,M = map(int, input().split())
recur(0)