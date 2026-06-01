def solution(n):
    answer = 0 # 10진법으로 변환할 값
    temp = [] # 3진법으로 변환한 값 리스트
    while n > 0: # 3진법으로 변환
        temp.append(n % 3) # 3으로 나눈 나머지를 리스트에 추가
        
        n //= 3 # 3으로 나눈 몫을 n에 저장
    temp.reverse() # 앞뒤반전(3진법)
    for i in range(len(temp)): # 10진법으로 변환
        answer += temp[i] * (3 ** i) # 3의 i승을 곱해서 10진법으로 변환
    return answer