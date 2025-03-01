def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        or_result = bin(arr1[i] | arr2[i]) #or 연산
        
        binary_str = or_result[2:] # 앞에 있는 0x 시작하는 부분 삭제
        
        padded_str = binary_str.zfill(n) #길이가 n이 되도록 왼쪽에 0을 채워줌
        
        padded_str = ''.join(['#' if x == '1' else ' ' for x in padded_str]) # 1이면 #, 0이면 공백
        answer.append(padded_str) #리스트에 각각 결과 삽입
    return answer