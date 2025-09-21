# 백준 15721번(번데기)
# 완전탐색

A = int(input())
T = int(input())
sign = int(input())

games = []  # 게임에서 외친 단어들을 (차례 번호, 단어 종류) 형태로 저장
b = 1 #'뻔' 횟수
d = 1 #'데기' 횟수
r = 0  # 라운드 수

while True:
    prev = b
    r += 1
    
    # 1) 기본 패턴: "뻔 - 데기 - 뻔 - 데기"
    for _ in range(2):
        games.append((b,0))
        b += 1
        games.append((d,1))
        d += 1
    
    # 2) 라운드마다 반복 증가하는 "뻔" 부분 (r + 1번 반복)
    for _ in range(r + 1): 
        games.append((b,0))
        b += 1
     # 2) 라운드마다 반복 증가하는 "데기" 부분 (r + 1번 반복)
    for _ in range(r + 1): 
        games.append((d,1))
        d += 1
    
    # 4) 이번 라운드에서 목표 T가 포함되었는지 확인
    #    (prev ≤ T < b 라는 조건은, 이번 라운드에 새로운 '뻔'이 추가된 구간임을 의미)
    if (prev <= T < b):
        print(games.index((T,sign)) % A)
        print(b,d)
        break