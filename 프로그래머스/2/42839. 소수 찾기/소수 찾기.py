from itertools import permutations
import math

def is_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    
    return True

def solution(numbers):
    cnt = 0
    num_list = [number for number in numbers]
    num_set = set()
    for i in range(1, len(num_list) + 1):
        for j in permutations(num_list, i):
            num = int(''.join(j))
            num_set.add(num)

    for num in num_set:
        result = is_prime(num)

        if result:
            cnt += 1
    
    return cnt