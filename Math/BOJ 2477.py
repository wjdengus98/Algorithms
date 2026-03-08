# 백준 참외밭
# 문제 풀기 Tip 
# 큰 직사각형: 큰 직사각형 = max_width * max_height
# 작은 직사각형 = 중간 인덱스의 가로 * 중간 인덱스의 세로

k = int(input())

sides= [list(map(int,input().split())) for _ in range(6)]

max_width, max_height = 0,0

for side in sides:
    move, length = side
    #가로(동/서)에서 최댓값 찾기
    if (move == 1 or move == 2) and length > max_width :
        max_width = length
    #세로(남/북)에서 최댓값 찾기
    if (move == 3 or move == 4) and length > max_height:
        max_height = length

small_sides = []

for i in range(6):
    # 현재 변과 2칸 뒤의 변의 방향 같은 지 확인
    if sides[i][0] == sides[(i+2)%6][0]:
        # 중간 인덱스의 길이가 B의 변
        small_sides.append(sides[(i+1)%6][1])
    
s_width, s_height = small_sides[0],small_sides[1]
        
big_rec = max_width * max_height
small_rec = s_width * s_height
area = big_rec - small_rec

print(area * k)