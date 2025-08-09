def solution(numbers):
    alphanum = [str(n) for n in numbers]
    alphanum.sort(key=lambda x: x*4, reverse=True) # 반복 키로 정렬
    result = "".join(alphanum)
    return str(int(result))