# 백준
# 평행사변형
# AB BC AC를 크기 순으로 정렬 후
# 가장 큰 둘레: (AC + BC) * 2
# 가장 작은 둘레: (AB + BC) * 2
import math

x1,y1,x2,y2,x3,y3 = map(int,input().split())

# 주어진 세 점이 일직선인 경우 -1 반환
if (x2 - x1) * (y3 - y2) == (x3 - x2) * (y2 - y1):
    print(-1)
else:
    # 각 변의 길이 계산
    AB = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    BC = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
    AC = math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)
    
    # 리스트에 넣고 오름차순 정렬(가장 작은 변 부터)
    triple_dot = [AB, BC, AC]
    triple_dot.sort()
    
    # 가장 큰 둘레
    longer_parimeter = (triple_dot[2] + triple_dot[1]) * 2
    
    # 가장 작은 둘레
    small_parimeter = (triple_dot[1] + triple_dot[0]) * 2
    
    # 둘레 길이의 차이
    diff = longer_parimeter - small_parimeter
    # 10^-9까지 출력 허용    
    print(f"{diff:.9f}")
