"""딕셔너리와 set을 쓰면 시간복잡도 o(1)으로 줄일 수 있다"""
def solution(topping):
    left = set() # 철수 
    right = {} # 동생
    cnt = 0 # 공평하게 나누는 거 세는 카운터
    
    # 처음에는 동생이 다 가짐
    for t in topping:
        if t not in right:
            right[t] = 1
        else:
            right[t] += 1
    
    for t in topping:
        left.add(t) # 형이 토핑하나씩 추가
        
        right[t] -= 1 # 동생의 토핑 삭제
        if right[t] == 0: #동생 토핑 다 떨어질 시 삭제
            del right[t] 
    
        if len(left) == len(right):
            cnt += 1
    return cnt