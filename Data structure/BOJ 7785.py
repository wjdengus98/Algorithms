#백준 7785번

n = int(input())
company = set()  # 중복을 방지하기 위해 set 사용

for _ in range(n):
    name, status = input().split()  # 입력에서 이름과 상태 분리
    if status == "enter":
        company.add(name)  # 출근 시 회사에 추가
    else:
        company.remove(name)  # 퇴근 시 회사에서 제거

# 현재 회사에 남아있는 사람들을 사전 역순으로 정렬
company = sorted(company, reverse=True)

# 결과 출력
for name in company:
    print(name)
