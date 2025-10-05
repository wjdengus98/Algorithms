def solution(elements):
    n = len(elements) # 원형수열의 길이
    
    elements = 2 * elements # 원형 수열 처리를 위해 리스트를 두 번 이어 붙임
    extended = set()
    
    # 부분 수열의 길이를 1부터 n까지 바꾸며 탐색
    for length in range(1, n+1):
        # 각 길이에 대해 시작 위치를 0 ~ n-1 까지 탐색
        for start in range(n):
            total = sum(elements[start:start+length]) # start부터 start+length까지의 연속 부분 수열 합 계산
            extended.add(total) # 부분합을 집합에 추가 (자동으로 중복 제거)
    return len(extended) # 부분합 개수 반환
