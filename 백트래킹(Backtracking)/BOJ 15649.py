#백준 알고리즘
# N과 M(1)
# 자연수 N과 M이 주어졌을 대, 아래 조건을 만족하는 길이가 M인 수열을 구하는 프로그램 작성
#조건: 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

arr = []

def recur(count):
    if count == M:
        print(*arr)
        return
    
    for i in range(1, N+1):
        if i not in arr: #중복 확인
            arr.append(i) # 배열 추가
            recur(count+1) # 재귀
            arr.pop() # return으로 돌아올 때 마지막 원소 삭제 이걸 안하면 배열에 계속해서 숫자가 쌓임

N, M = map(int, input().split())  # N은 숫자 범위, M은 수열의 길이

recur(0)
