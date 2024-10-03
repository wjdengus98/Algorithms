#백준 1620번(포켓몬 마스터 이다솜)

problem = {} #문제도감
answer = [] 

n, m= map(int,input().split())


for index in range(1, n+1):
    pk = input()
    #양방향 딕셔너리로 설정: 키,값 조회 모두 가능! 키-->값, 값--->키
    problem[str(index)] = pk
    problem[pk] = str(index)


for _ in range(m):
    ans = input()
    print(problem[ans])
    




