
dirs = "ULURRDLLU"

direction = {
    "U" : 0,
    "D" : 1,
    "R" : 2,
    "L" : 3
}

dx = [-1,1,0,0]
dy = [0,0,1,-1]

def solution(dirs):
    x,y = 0,0
    visited = set()
    for d in dirs:    
        idx = direction[d]
        nx = x + dx[idx]
        ny = y + dy[idx]
        
        if nx > 5 or nx < -5 or ny < -5 or ny > 5:  # 격자판을 벗어나는 경우 제외
            continue
        # 양 방향 까지 추가 A->B로 가나 B->A로 가나 같다
        visited.add((x,y,nx,ny))
        visited.add((nx,ny,x,y))
        
        x,y = nx, ny # 방향 업데이트
        
    return len(visited) // 2 # 양 방향은 1개의 처음 간 길로 지정