# SWEA - 컨테이너 운반

TC = int(input())

for t in range(TC):
    N,M = map(int,input().split()) # 컨테이너 개수: N, 트럭 개수: M
    
    lst1 = list(map(int,input().split())) # 각 컨테이너의 무게
    lst2 = list(map(int,input().split())) # 각 트럭의 적재 용량 리스트
    
    # 무거운 컨테이너, 트럭 처리하기 위해서 내림차순 정렬
    lst1.sort(reverse=True) 
    lst2.sort(reverse=True)
        
    ans = 0 #무게의 합
    i = 0 # 사용 중인 트럭 인덱스
    
    for n in lst1: # 컨테이너의 무게 중
        if n <= lst2[i]: # 트럭이 감당 가능하면
            ans += n # 무게를 더하고
            i += 1 # 그 다음 트럭으로 이동
            if i == M: # 만약 트럭을 다 사용했으면 
                break # 종료
            
    print(f"#{t + 1} {ans}")