#백준 2017 연세대학교 프로그래밍 경시대회

n = int(input())

cnt = 0

for a in range(0,n+1): #A: 0개 ~ N개
    for b in range(0, n+1): #B: 0개 ~ N개
        for c in range(0, n+1): #C: 0개 ~ N개
            if a+b+c == n: #남는 사탕이 없어야 한다!
                if a >= b+2: # 남규는 영훈이보다 2개 이상 많은 사탕
                    if a != 0 and b != 0 and c!= 0: # 하나도 못 받는 친구 없어야함
                        if c % 2 == 0: # 택희가 받는 사탕의 수는 짝수
                            cnt += 1
print(cnt)
