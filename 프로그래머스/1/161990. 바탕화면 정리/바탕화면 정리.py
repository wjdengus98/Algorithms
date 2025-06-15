def solution(wallpaper):
    min_row, min_col = 100,100 # 최소 (행,열)
    max_row, max_col = -1,-1 #최대 (행,열)
    
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == "#": # "#"을 만나면
                min_row = min(i, min_row) #최소행 갱신
                min_col = min(j, min_col) #최소열 갱신
                max_row = max(i, max_row) #최대행 갱신
                max_col = max(j, max_col) #최대열 갱신 
     
    return [min_row, min_col, max_row + 1, max_col + 1]  #최대행에만 1을 더하여 출력