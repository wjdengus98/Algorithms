def solution(n,w,num):
    h = (n // w) + 1
    storages = []
    val = 1

    for i in range(h):
        box = []
        for j in range(w):
            if val <= n:
                box.append(val)
                val += 1
            else:
                box.append(0)
        
        if i % 2 == 1: # i = 1, 3일 때 역순으로 뒤집어 지그재그 구현하기
            box.reverse()
        
        storages.append(box)
    

    # 밑으로 추적하기
    target_r, target_c = -1,-1
    for r in range(h):
        for c in range(w):
            if storages[r][c] == num:
                target_r = r
                target_c = c
                break
        if target_r != -1:
            break
    
    cnt = 0
    for r in range(target_r, h):
        if storages[r][target_c] != 0:
            cnt += 1
    
    return cnt