# 정수 N이 주어질 때
# 1에서 정수 N까지의 합이 10이 되는 경우를 모두 출력한다
# 백트래킹

n = int(input())

def backtracking(sum,selected_num,start,N,results):
    if sum == 10:
        results.append(selected_num)
        return
    for i in range(start, N+1):
        if sum + i <= 10:
            backtracking(sum + i, selected_num + [i], i+1,N, results)

def solution(n):
    result = []
    backtracking(0,[],1,n,result)
    return result

print(solution(n))