def solution(s):
    cnt = 0
    times = 0
    
    while s != "1": #문자열이 1이 될때까지 반복!
        i = 0
        
        zero = s.count("0") #0의 개수 세기
        s = s.replace("0", "") #전부 1로 변환
        cnt += zero #0의 개수 누적
        
        lth = len(s)
        
        s = bin(lth)[2:] #2진법 변환
        print(f"s: {s}")
        
        times += 1 # 이진 변환 횟수 증가
    return [times, cnt] #  # [이진 변환 횟수, 제거된 0의 총 개수]를 반환
        
        

# s = "110010101001"
# print(solution(s))
        