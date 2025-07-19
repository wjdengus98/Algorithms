# 백준 알고리즘 - 5555번
# 반지
# https://www.acmicpc.net/problem/5555

# 1. 찾고자 하는 문자열 입력
target = input().strip()

# 2. 반지 개수 입력
n = int(input())

# 3. 카운터 초기화
count = 0

# 4. 각 반지에 대해 확인
for _ in range(n):
    ring = input().strip()
    doubled_ring = ring + ring  # 회전을 고려한 확장
    if target in doubled_ring:
        count += 1

# 5. 결과 출력
print(count)
