# 백준 1015번
# 수열 정렬
# https://www.acmicpc.net/problem/1015

import sys
input = sys.stdin.readline

N = int(input()) # N은 수열의 길이
A = list(map(int,input().split()))  # 수열 A
sorted_A = sorted(A) # 오름차순으로 정렬된 수열


P = [] # P[i]는 A[i]가 정렬된 수열에서 몇 번째 위치에 있는지 저장하는 리스트
# 예를 들어, A = [3, 1, 2] 이면 sorted_A = [1, 2, 3] 이고 P = [2, 0, 1]이 된다.
for i in range(N):
    P.append(sorted_A.index(A[i])) # 중복된 값이 있을 경우 첫 번째 인덱스만 반환되므로, 중복된 값은 -9999로 대체
    sorted_A[sorted_A.index(A[i])] = -9999
    
for j in range(len(P)):
    print(f"{str(P[j])}", end=" ")