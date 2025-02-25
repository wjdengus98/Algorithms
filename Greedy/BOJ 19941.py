# 백준 알고리즘 - 19941번
# https://www.acmicpc.net/problem/19941

import sys
input = sys.stdin.readline
n, k = map(int,input().split())
length = list(input().strip())
cnt = 0

for i in range(n):
    if length[i] == 'P': # 현재 P자리 사람이면
            for j in range(i-k, i+k+1): # 현재 P자리 사람이 먹을 수 있는 햄버거 범위
                if j < 0 or j >= n: # 인덱스 범위 밖이면 무시
                    continue
                if length[j] == 'H': #햄버거 자리이면
                    cnt += 1 # 햄버거 먹은 사람 증가
                    length[j] = 'X' # 먹은 햄버거 표시
                    break

print(cnt)