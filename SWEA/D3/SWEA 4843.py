T = int(input())

for t in range(1, T + 1):
    N = int(input())
    arr = list(map(int,input().split()))
    
    # 1. 오름차순 정렬
    arr.sort()
    
    # 2. 특별한 정렬을 위한 리스트
    res = []
    
    # 3. 큰 수, 작은 수 번갈아 가며 추가하기(10개까지)
    for i in range(5):
        if len(arr) > 0:
            res.append(arr[-1]) # 가장 큰 수 먼저 추가
            arr.pop(-1)
        if len(arr) > 0:
            res.append(arr[0]) # 가장 작은 수 추가
            arr.pop(0)
            
    print(f"#{t}", *res) #출력