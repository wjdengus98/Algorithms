# 백준 알고리즘 - 한수
# 1065번

n = int(input()) # 1 이상 1000 이하의 정수

hansu = 0 # 한수의 개수

for i in range(1, n+1): 
    if i <= 99: # 1부터 99까지는 모두 한수
        hansu += 1
    else: # 100부터는 각 자리수가 등차수열을 이루는지 확인
        nums = list(map(int, str(i))) # 숫자를 자릿수대로 분리
        if nums[0] - nums[1] == nums[1] - nums[2]: # 등차수열 확인
            hansu += 1

print(hansu) # 결과 출력