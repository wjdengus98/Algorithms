#서브트리(Subtree)

#전위 순회 함수 구현현
def preord(n):
    global cnt
    if n: #노드가 존재하면
        cnt += 1 # 카운트
        preord(ch1[n]) #왼쪽 자식 노드 순회
        preord(ch2[n]) #오른쪽 자식 노드 순회회

T = int(input())
for i in range(1, T+1):
    E,S = map(int,input().split())
    lst = list(map(int,input().split()))
    
    # [1] 트리를 저장
    ch1 = [0] * (E+2) # 왼쪽 자식 노드 정보를 저장하는 배열
    ch2 = [0] * (E+2) # 오른쪽 자식 노드 정보를 저장하는 배열

    # 입력받은 간선 정보 리스트를 순회
    for j in range(0, len(lst), 2):
        p,c = lst[j], lst[j+1]
        if ch1[p] == 0:
            ch1[p] = c
        else:
            ch2[p] = c
            
    cnt = 0
    preord(S)
    
    print(f"#{i} {cnt}")