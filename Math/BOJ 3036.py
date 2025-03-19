# 백준 알고리즘 - 3036번
# 링

import math
n = int(input()) # 링의 개수

nums = list(map(int, input().split())) # 링의 반지름 리스트

for i in range(1,n): #출력은 n-1번만 해야함
    gcd = math.gcd(nums[0], nums[i]) # 최대공약수
    print(str(nums[0] // gcd) + '/' + str(nums[i] // gcd)) # 최대공약수로 나눈 값 출력