# 10진수 -> n진수로 변환
def convert(n,base):
    arr = "0123456789ABCDEF"
    q,r = divmod(n,base)
    if q == 0:
        return arr[r]
    else:
        return convert(q,base) + arr[r]
    

def solution(n, t, m, p):
    words=""
    i = 0
    
    while len(words) < t * m:
        words += convert(i,n)
        i += 1
    
    answer = ""
    while(len(answer) < t):
        answer += words[p-1]
        p += m
    
    return answer