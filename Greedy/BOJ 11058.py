# 백준
# 2+1 세일

N= int(input())

prices = [int(input()) for i in range(N)]

# 비싼 것 부터 정렬
prices.sort(reverse=True)

# 3개씩 묶었을 때 가장 저렴한 것(인덱스 2,5,8...)이 무료
print(sum(prices) - sum(prices[2::3]))

    