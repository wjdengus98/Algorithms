# 백준 - 20546번
# 기적의 매매법
# https://www.acmicpc.net/problem/20546

money = int(input()) #현금금
prices = list(map(int,input().split())) #가격
 
stock1, cash1 = 0,0 #주식 수, 캐쉬

length = len(prices) #주식 리스트 길이

# 1. 준현이의 주식가격
stock1 = 0
cash1 = money

for i in range(length):
    if cash1 >= prices[i]:
        buy = cash1 // prices[i]
        stock1 += buy
        cash1 -= buy * prices[i]

Junhyun = cash1 + (stock1 * prices[-1])

# Sungmin이의 주식가격
stock2 = 0
cash2 = money

for i in range(3, length):
    # 3일 연속 상승 → 매도
    if prices[i - 3] < prices[i - 2] < prices[i - 1]:
        if stock2 > 0:
            cash2 += stock2 * prices[i]
            stock2 = 0
    # 3일 연속 하락 → 매수
    elif prices[i - 3] > prices[i - 2] > prices[i - 1]:
        buy = cash2 // prices[i]
        stock2 += buy
        cash2 -= buy * prices[i]

# 마지막 날 자산 평가
Sungmin = cash2 + (stock2 * prices[-1])


if Junhyun > Sungmin:
    print("BNP")
elif Junhyun < Sungmin:
    print("TIMING")
else:
    print("SAMESAME")
    
    
    

    

        