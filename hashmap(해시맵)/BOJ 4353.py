# 백준 4353
# 생태학
# https://www.acmicpc.net/problem/4358

import sys

input = sys.stdin.readline

_dict = {} #나무의 빈도수를 저장할 딕셔너리
cnt = 0 #나무의 총 개수

while True:
    tree = input().rstrip() #나무 입력
    if not tree: #문자가 입력되지 않으면 
        break # 종료
    
    if tree in _dict: #딕셔너리에 나무 존재
        _dict[tree] += 1 # 카운트 증가
    else: #존재하지 않으면
        _dict[tree] = 1 #딕셔너리 추가
    cnt += 1

sorted_tree = sorted(_dict.keys()) #딕셔너리의 키(나무) 정렬

for t in sorted_tree:
    print(f"{t} {(_dict[t] / cnt) * 100:.4f}") #f-string을 이용한 소숫점 4째 자리까지 출력력
        