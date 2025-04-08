from itertools import combinations

def is_prime(n): #소수 판별 알고리즘
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(nums):
    cmb_list = list(combinations(nums,3)) #주어진 숫자중 3개의 수 선정
    numbers = [] #3개의 수들의 합 리스트
    
    for i in range(len(cmb_list)):
        numbers.append(sum(cmb_list[i])) #합을 리스트에 넣는다
    
    prime_count = sum([1 for num in numbers if is_prime(num)]) #소수일때마다 카운트
    
    return prime_count