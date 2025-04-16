# 백준 알고리즘 - 색종이 만들기
# https://www.acmicpc.net/problem/2630
# 문제 설명: 색종이의 크기 n*n을 입력받고, 색종이가 모두 같은 색인지 확인하는 프로그램을 작성하시오.

def checkSameColor(x,y,size): # 색종이의 색이 모두 같은지 확인하는 함수
    color = arr[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if arr[i][j] != color:
                return False
    return True
    
def myExecute(x, y, size):
    color = arr[x][y] # 색종이의 색을 저장
    same = checkSameColor(x, y, size) # 색종이가 모두 같은 색인지 확인    
    if same: # 색종이가 모두 같은 색일 경우
        if color == 0: # 색종이가 하얀색일 경우
            global white
            white += 1 # 하얀색 종이 개수 증가
        else: # 색종이가 파란색일 경우
            global blue
            blue += 1
    else: # 다른 값이면 4등분해서 다시 검색
        size = size // 2
        myExecute(x, y, size) # 왼쪽 위
        myExecute(x + size, y, size) # 오른쪽 위
        myExecute(x, y + size, size) # 왼쪽 아래
        myExecute(x + size, y + size, size) # 오른쪽 아래
        
import sys
sys.setrecursionlimit(10**6) # 재귀 깊이 설정

N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] # 색종이 배열 입력받기
white = 0 #하얀색 종이 개수
blue = 0 #파란색 종이 개수

myExecute(0, 0, N) # 색종이 개수 세기

print(white) # 하얀색 종이 개수 출력
print(blue) # 파란색 종이 개수 출력
