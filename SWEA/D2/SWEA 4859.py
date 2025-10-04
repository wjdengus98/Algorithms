# 4839. [파이썬 S/W 문제해결 기본] 2일차 - 이진탐색

T = int(input())

def Bsearch(total, find):
    l = 1
    r = total
    cnt = 0
    
    while l <= r:
        c = (l + r) // 2
        cnt += 1
        
        if c == find:
            return cnt
        elif c < find:
            l = c 
        else:  # c > find
            r = c 
    
    return 0  # 찾지 못한 경우
            
            
for i in range(T):
    page,pa,pb = map(int,input().split())
    
    A = Bsearch(page,pa)
    B = Bsearch(page,pb)
    
    if A < B:
        print(f"#{i+1} A")
    elif A > B:
        print(f"#{i+1} B")
    elif A == B:
        print(f"#{i+1} 0")
    
    