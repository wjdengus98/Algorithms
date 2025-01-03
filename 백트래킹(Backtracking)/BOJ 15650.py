#백준 N과 M(2)

arr = []

def recur(count,start):
    if count == M:
        print(*arr)
        return
    
    # start부터 N까지의 숫자를 순회
    for i in range(start, N+1):
        arr.append(i) # i를 선택하고 arr에 추가
        recur(count+1,i+1) # 선택한 숫자를 포함하여 재귀 호출 (다음 숫자는 i+1부터 시작)
        arr.pop() # 재귀 호출 이후 선택한 숫자를 제거하여 이전 상태로 복원
        
N,M = map(int, input().split())

recur(0,1)