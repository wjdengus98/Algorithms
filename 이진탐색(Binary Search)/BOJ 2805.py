# 백준 알고리즘 - 2805번
# 나무 자르기
import sys
input = sys.stdin.readline
N,M = map(int, input().split())
trees = list(map(int, input().split()))

high, low = max(trees),0 # 나무의 최대 높이와 0으로 초기화
answer = 0 # 자른 나무의 높이

# 이진 탐색을 통해 나무를 자르는 높이 찾기.
while low <= high:
    mid = (high + low) // 2 # 중간 높이
    cnt = 0 # 나무를 자르고 얻을 길이
    
    for tree in trees:
        if tree > mid: # 나무가 자를 높이보다 크면
            cnt += tree - mid # 자른 길이 추가
    if cnt >= M: # 자른 길이가 M보다 크거나 같으면
        answer = mid # 높이 저장
        low = mid + 1 # 더 높은 높이 탐색
    else: # 자른 길이가 M보다 작으면
        high = mid - 1 # 낮은 높이 탐색
        
print(answer)