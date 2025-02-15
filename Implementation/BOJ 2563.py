#백준 2563번(색종이)

n = int(input())
paper = [[0] * 101 for _ in range(101)] #2차원 리스트 생성

for _ in range(n):
    x,y = map(int,input().split())
    
    for i in range(x, x+10):
        for j in range(y, y+10): 
            paper[i][j] = 1 #색종이가 붙은 부분 1로 표시
    

cnt = 0 #1의 개수를 세기 위한 변수
for i in range(101):
    for j in range(101):
        if paper[i][j] == 1:
            cnt += 1

print(cnt) #결과 출력