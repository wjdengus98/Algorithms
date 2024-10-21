#백준 문자열 집합

import sys

n, m = map(int, input().split())

s = set()  # 집합 s 선언 (N개의 문자열 저장)
cnt = 0  # 집합 S에 포함되어 있는 문자열 개수

for _ in range(n):
    s.add(sys.stdin.readline().strip())  # N개의 문자열을 집합 s에 추가

for _ in range(m):
    word = sys.stdin.readline().strip()  # M개의 문자열을 입력받음

    if word in s:  # 입력받은 단어가 집합 s에 포함되어 있는지 확인
        cnt += 1

print(cnt)
