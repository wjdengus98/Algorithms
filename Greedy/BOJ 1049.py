# 백준 알고리즘 - 1049번
# 기타줄

n, m = map(int, input().split())
pack = []  # 패키지 가격 리스트
one = []   # 낱개 가격 리스트

for _ in range(m):
    a, b = map(int, input().split())  # 패키지 가격, 낱개 가격
    pack.append(a)
    one.append(b)

# 최소 패키지 가격과 최소 낱개 가격을 루프 바깥에서 계산
min_pack = min(pack)
min_one = min(one)

# 낱개로 사는 것이 더 저렴한 경우
if min_one * 6 < min_pack:
    print(min_one * n)
else:
    # 6개 묶음 단위로 계산
    if n % 6 == 0:
        print(min_pack * (n // 6))
    else:
        # 남은 개수를 패키지로 사는 게 나은지, 낱개로 사는 게 나은지 비교
        print(min(min_pack * ((n // 6) + 1), min_pack * (n // 6) + min_one * (n % 6)))
