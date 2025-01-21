#백준 동전0
N, K = map(int, input().split())
cnt = 0
coin_type  = []

for i in range(N):
    coin_type.append(int(input()))

coin_type.sort(reverse = True)

for coin in coin_type:
    if K == 0:
        break
    cnt += K // coin
    K %= coin

print(cnt)
    