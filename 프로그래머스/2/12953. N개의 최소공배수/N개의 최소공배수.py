
def solution(arr):
    import math
    
    # 첫 번째 원소로 초기화
    answer = arr[0]
    
    # 두 번째 원소부터 순차적으로 최소공배수 계산
    for i in range(1, len(arr)):
        answer = (answer * arr[i]) // math.gcd(answer, arr[i])
    
    return answer