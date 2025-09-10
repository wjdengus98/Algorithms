# 삼성 EXPERT 아카데미
# 5108번 
# 숫자 추가

T = int(input())

for i in range(T):
    N,M,L = map(int,input().split())
    arr = list(map(int,input().split()))
    
    for j in range(M):
        a,b = map(int,input().split())
        
        rest = arr[a::]
        for _ in range(N-a):
            arr.pop()

        arr.append(b)
        arr = arr + rest
        N += 1
 
        
    print(f"#{i + 1} {arr[L]}")
        

    
    