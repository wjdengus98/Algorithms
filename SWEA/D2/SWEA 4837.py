from itertools import combinations

T = int(input())
A = [1,2,3,4,5,6,7,8,9,10,11,12]

for i in range(T):
    N,K = map(int,input().split())
    
    parts = list(combinations(A,N))
    cnt = 0
    
    for p in parts:
        if sum(p) == K:
            cnt += 1
    
    print(f"#{i+1} {cnt}")