# 백준 알고리즘 - 10986번
# 나머지 합

import sys
input = sys.stdin.readline
n,m = map(int,input().split()) # n: 수열의 길이, m: 나눌 수
A = list(map(int,input().split())) # 원본 수열 저장 리스트
S = [0] * n # 누적합 저장 리스트
C = [0] * m # 나머지 저장 리스트
answer = 0 # 정답 저장 변수

S[0] = A[0] # 첫번째 원소는 그대로 저장

for i in range(1, n):
    S[i] = S[i - 1] + A[i] # 누적합 계산

for i in range(n):
    remainder = S[i] % m # 나머지 계산
    if remainder == 0: # 나머지가 0이면 정답에 1 더함
        answer += 1
    C[remainder] += 1 # 나머지 저장

for i in range(m):
    if C[i] > 1: #나머지 배열에 있는 수가 2이상이면
        answer += C[i] * (C[i] - 1) // 2 #조합 계산 2개만 뽑으면 경우의 수가 나온다

print(answer) # 정답 출력