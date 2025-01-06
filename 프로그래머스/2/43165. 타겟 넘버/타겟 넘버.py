def dfs(idx, total, target, numbers):
    # dfs 호출로 결과 반환
    count = 0 # 카운트 초기화
    if idx == len(numbers): # 모든 숫자를 탐색한 경우
        if total == target: # 합계가 목표값과 같으면
            count += 1 # 카운트 증가
        return count  # 카운트 반환
    # 재귀 호출로 count 누적
    count += dfs(idx+1, total + numbers[idx], target, numbers) #현재 숫자 더하는 경우
    count += dfs(idx+1, total - numbers[idx], target, numbers) #현재 숫자 빼는 경우
    
    return count # 누적된 카운트를 반환
    
def solution(numbers, target):
    answer = dfs(0,0,target,numbers)
    return answer