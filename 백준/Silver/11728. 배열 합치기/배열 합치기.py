#백준 배열 합치기
# 배열 A와 B를 합쳐서 정렬하는 문제

import sys

n,m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

a.extend(b)
a.sort()

print(*a)