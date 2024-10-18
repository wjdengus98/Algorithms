#백준 듣보잡(1764)

n,m = map(int, input().split())

a = set() #듣도 못한 사람 집합
b = set() #보도 못한 사람 집합

for i in range(n):
    a.add(input())

for i in range(m):
    b.add(input())
    

results = sorted(a.intersection(b)) #a와 b에 공통으로 들어있는 사람(사전순 정렬)

print(len(results)) #듣보잡의 수 출력

for result in results: #사전순으로 출력하기
    print(result)