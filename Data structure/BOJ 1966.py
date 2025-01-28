#프린터 큐
from collections import deque

t = int(input())

for _ in range(t):
    n,m = map(int,input().split())
    s = list(map(int,input().split()))
    q = deque() #큐 선언
    
     # 문서 번호와 중요도를 큐에 저장
    for i,x in enumerate(s):
        q.append((i,x))
        
    s.sort() #중요도 정렬렬
    
    cnt = 0 # 인쇄 순서
    
    while q:
        i,x = q.popleft() # 큐의 첫 번째 문서 꺼내기
        
         # 현재 문서가 가장 높은 중요도를 가지지 않는 경우
        if x < s[-1]:
            q.append((i,x)) # 문서를 다시 큐의 뒤로 보냄
        else:# 현재 문서를 인쇄
            cnt += 1
            s.pop()
            
             # 목표 문서인 경우 출력
            if i == m:
                print(cnt)
                break
        
        
    