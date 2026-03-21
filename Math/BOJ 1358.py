# 백준 1358번
# 하키
import math

W,H,X,Y,P = map(int,input().split())

radius = H // 2
cnt = 0

for _ in range(P):
    PX,PY = map(int,input().split())
    
    d1 = math.sqrt((PX - X)**2 + (PY - (Y + radius))**2) # 첫번째 원과의 거리
    d2 = math.sqrt((PX - (X+W))**2 + (PY - (Y + radius))**2) # 두번재 원과의 거리
    
    if X <= PX <= X + W and Y <= PY <= Y + H: # px,py가 직사각형 범위 통과시 
        cnt += 1 # 카운터 증가
        
    elif d1 <= radius: # px,py가 첫번째 원 안에 포함 시
        cnt += 1 # 카운터 증가
        
    elif d2 <= radius: # px,py가 두번째 원 안에 포함 시
        cnt += 1 # 카운터 증가

print(cnt)