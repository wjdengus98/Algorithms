#백준 두 수의 합
import sys

n = int(input()) # 입력받을 값의 개수

num_list = list(map(int, input().split())) # 입력받은 값들을 리스트로 저장

x = int(input()) # 찾고자 하는 값

num_list.sort() # 정렬

s = 0 # 시작 인덱스
e = len(num_list) - 1 # 끝 인덱스
cnt = 0 # 조건에 맞는 쌍의 개수

# 투 포인터 알고리즘즘
while s < e:
    if (num_list[s] + num_list[e] == x):
        cnt += 1
        e -= 1
    elif (num_list[s] + num_list[e] > x):
        e -= 1
    else:
        s += 1

print(cnt)
    