#백준 상금 헌터

def a_prize(a):
    if a == 0:
        return 0
    prize_table = [(1, 5000000), (3, 3000000), (6, 2000000), (10, 500000), (15, 300000), (21, 100000)]
    for limit, prize in prize_table:
        if a <= limit:
            return prize
    return 0
    

def b_prize(b):
    if b == 0:
        return 0
    prize_table = [(1, 5120000), (3, 2560000), (7, 1280000), (15, 640000), (31, 320000)]
    for limit, prize in prize_table:
        if b <= limit:
            return prize
    return 0
    

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    price = a_prize(a) + b_prize(b)
    print(price)
