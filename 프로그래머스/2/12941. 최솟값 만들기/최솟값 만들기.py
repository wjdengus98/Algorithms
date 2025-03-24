def solution(A,B):
    #최소값 만들기 A 오름차순 정렬, B 내림차순 정렬.
    #각각의 인덱스 자리를 곱한다
    
    A.sort()
    B.sort(reverse = True)
    tot = 0
    for i in range(len(A)):
        tot += A[i] * B[i]
    return tot
