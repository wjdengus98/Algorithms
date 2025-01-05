#N과 M(3) 백준 15651
# 중복 없이 나열
#N과 M(1)에서 했던 중복 제거 알고리즘을 지우면 됨

arr = []

def recur(count):
    if count == M:
        print(*arr)
        return
    
    for i in range(1, N+1):
            arr.append(i) # 배열 추가
            recur(count+1) # 재귀
            arr.pop() # return으로 돌아올 때 마지막 원소 삭제 이걸 안하면 배열에 계속해서 숫자가 쌓임

N, M = map(int, input().split())  # N은 숫자 범위, M은 수열의 길이

recur(0)