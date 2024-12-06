#백준 17219번

# 입력 받기
N, M = map(int, input().split())

# 해시맵(딕셔너리) 생성
password_dict = {}
for _ in range(N):
    site, password = input().split()
    password_dict[site] = password

# 쿼리 처리 및 결과 출력
for _ in range(M):
    query = input()
    print(password_dict[query])
