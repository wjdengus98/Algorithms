import sys
input = sys.stdin.readline

n = int(input())  # 수열의 크기
num_list = list(map(int, input().split()))  # 수열
sum_list = [0] * (n + 1)  # 누적합 리스트

# 누적합 리스트 생성
for i in range(1, n + 1):
    sum_list[i] = sum_list[i - 1] + num_list[i - 1]  # 누적합

m = int(input())  # 구간의 개수

for _ in range(m):
    i, j = map(int, input().strip().split())
    print(sum_list[j] - sum_list[i - 1])  # 구간의 합 출력
