# 백준 알고리즘 - 2847번
# https://www.acmicpc.net/problem/2847

import sys
input = sys.stdin.readline

n = int(input()) # 레벨의 수
scores = [] # 레벨의 점수를 담을 리스트트

for i in range(n): 
    scores.append(int(input())) # 레벨의 점수 입력

cnt = 0 # 조정 횟수

# 뒤에서부터 앞으로 가면서 비교
for i in range(n-1,0,-1): # 뒤에서부터
    while scores[i] <= scores[i-1]: # 뒤의 값이 앞의 값보다 작을 때
        scores[i-1] -= 1 # 앞의 값에서 1을 빼준다
        cnt += 1 # 카운트 증가

print(cnt)
  