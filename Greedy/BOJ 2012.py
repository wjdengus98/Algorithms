# 백준 알고리즘 - 2012번
# 등수 매기기

import sys

n = int(sys.stdin.readline()) # 학생의 수

arr = sorted([int(sys.stdin.readline()) for _ in range(n)]) # 학생들의 등수를 담을 배열, 그리고 정렬

result = 0 # 불만도의 합

for i in range(1, n+1):
    result += abs(i - arr[i-1]) # 학생들의 등수와 순서의 차이를 더함

print(result) # 결과 출력
