# 백준 알고리즘 - 2828번
# 사과 담기 게임 
# https://www.acmicpc.net/problem/2828

N,M = map(int,input().split())
dist = 0 # 이동 거리
basket_left = 1 # 바구니의 왼쪽 끝(무조건 1)

amount = int(input()) # 사과의 개수

for i in range(amount):
    apple = int(input())
    basket_right = basket_left + M - 1 # 바구니의 오른쪽 끝
    
    # 바구니의 왼쪽 끝과 오른쪽 끝을 비교하여 사과를 담을 수 있는 위치를 결정
    if apple > basket_right: # 바구니의 오른쪽 끝보다 사과가 오른쪽에 있는 경우
        move = apple - basket_right #사과와 오른쪽 끝의 위치 차이
        dist += move # 이동 거리에 더함
        basket_left += move # 바구니 왼쪽 끝 이동
        basket_right += move # 바구니 오른쪽 끝 이동
        
    elif apple < basket_left: # 바구니의 왼쪽 끝보다 사과가 왼쪽에 있는 경우
        move = basket_left - apple #사과와 왼쪽 끝의 위치 차이
        dist += move # 이동 거리에 더함
        basket_left -= move # 바구니 왼쪽 끝 이동
        basket_right -= move # 바구니 오른쪽 끝 이동
        
print(dist)
    
