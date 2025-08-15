# 백준 수학숙제
# 2870번

n = int(input())
results = [] #결과 배열

for i in range(n):
    letter = input() #글자(숫자와 알파벳 섞여있음)
    num_str = ""
    
    for l in letter:
        if l.isdigit(): #숫자인 경우
            num_str += l #숫자 문자열 추가
        else: # 숫자가 아닌경우
            if num_str == "":
                continue
            results.append(int(num_str)) #그동안 모았던 숫자 문자열 추가
            num_str = "" #숫자 문자열 다시 초기화
    
    if num_str: # 마지막까지 남은 숫자 문자열
        results.append(int(num_str)) #결과 배열 추가
    
for result in sorted(results): #results에 있는 배열을 하나씩 꺼내서 출력 -> 비내림차순
    print(result)