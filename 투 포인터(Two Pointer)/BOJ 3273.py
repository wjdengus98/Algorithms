#백준 두 수의 합
import sys

n = int(input()) # 입력받을 값의 개수

num_list = list(map(int, input().split())) # 입력받은 값들을 리스트로 저장

x = int(input()) # 찾고자 하는 값

num_list.sort() # 정렬

s = 0 # 시작 인덱스
e = len(num_list) - 1 # 끝 인덱스
cnt = 0 # 조건에 맞는 쌍의 개수

# 투 포인터 알고리즘
while s < e:
    if (num_list[s] + num_list[e] == x): # 두 수의 합이 x와 같다면
        cnt += 1 # 조건에 맞는 쌍의 개수 1 증가
        e -= 1 # 끝 인덱스 1 감소
    elif (num_list[s] + num_list[e] > x): # 두 수의 합이 x보다 크다면
        e -= 1 # 끝 인덱스 1 감소
    else: # 두 수의 합이 x보다 작다면
        s += 1 # 시작 인덱스 1 증가

print(cnt) #결과 출력