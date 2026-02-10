# SWEA - 반복문자 지우기

T = int(input()) # 테스트 케이스 갯수

for i in range(T):
    strings = input()
    res = []
    
    for string in strings:
    
        if len(res) > 0:
            if res[-1] == string:
                res.pop()
                continue
            else:
                res.append(string)
        else:
            res.append(string)
    
    print(f"#{i+1} {len(res)}")
