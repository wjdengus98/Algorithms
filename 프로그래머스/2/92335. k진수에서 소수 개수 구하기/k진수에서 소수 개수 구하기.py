import math

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def solution(n, k):
    number = ''
    while n:
        b = n % k
        number = str(b) + number
        print(number)
        n = n // k
    number = number.split("0")
    res = []
    for num in number:
        if num == '':
            continue
        n = int(num)
        # 소수 알고리즘 판별
        result = is_prime(n)
        if result:
            res.append(n)
    return len(res)