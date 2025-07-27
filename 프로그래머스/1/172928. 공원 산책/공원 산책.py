park = ["SOO","OOO","OOO"]
routes = ["E 2","S 2","W 1"]

move = {'E': (1,0), 'W' : (-1,0), 'S' : (0,1), 'N': (0,-1)}

def solution(park, routes):
    # 공원을 2차원 배열으로 바꾸기
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == 'S':
                start = [i,j]
                break
    
    for route in routes:
        dir = route[0] # op
        num = int(route[2]) #n
        
        dx,dy = move[dir]
        ny, nx = start[0], start[1]
        
        is_valid = True
        
        #1칸식 이동해서 유효한지 체크하기
        for i in range(1, num + 1):
            ny += dy # [0,0] -> [0,1]을 만들려면 arr[y][x]로 설정
            nx += dx
            
            # 범위 벗어나는 경우
            if ny < 0 or ny >= len(park) or nx < 0 or nx >= len(park[0]):
                is_valid = False
                break
            
            # 장애물 만나는 경우
            if park[ny][nx] == 'X':
                is_valid = False
                break
            
        if is_valid: # is_valid가 참일때만 갱신
            start = [ny,nx]
    
    return start
        
        
        
            

print(solution(park, routes))