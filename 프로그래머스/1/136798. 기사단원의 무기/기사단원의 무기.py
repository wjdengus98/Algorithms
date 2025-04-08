def solution(number, limit, power):
    divisor = [0] * (number + 1)
    
    #약수의 개수 구하기
    for i in range(1, number+1):
        for j in range(i, number + 1, i):
            divisor[j] += 1
    
    # 공격력 제한 수치가 limit을 초과 -> 대체수로 바꿈
    for i in range(len(divisor)):
        if divisor[i] > limit:
            divisor[i] = power
    
    return sum(divisor)