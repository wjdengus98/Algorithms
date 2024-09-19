#백준 2506

n = int(input())

n_list = list(map(int,input().split()))

cnt = 0
result = 0
for i in range(n):
    if n_list[i] == 1:
        cnt += 1
        result += cnt
    else:
        cnt = 0

print(result)