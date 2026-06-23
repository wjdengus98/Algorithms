import math

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
        storages.append(box)
    

    # 밑으로 추적하기
    cnt = 0
    
    
    return storages