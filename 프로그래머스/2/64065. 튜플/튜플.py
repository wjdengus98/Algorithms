def solution(s):
    s = s[2:-2]  # 맨 앞 {{ 와 맨 뒤 }} 두 글자씩 제거
    sets = s.split("},{")
    sets.sort(key=lambda x:len(x))
    result = []
    
    for i in range(len(sets)):
        nums = sets[i].split(",")  # '2,1' → ['2', '1']
        for num in nums:
            n = int(num)
            if n not in result:  # 아직 없는 숫자만 추가
                result.append(n)
    
    return result 