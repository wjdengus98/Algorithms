#백준 보물 - 1026
# 아이디어: A와 B에 있는 수를 둘 다 정렬에서 대각선으로 각각 곱한다!

n = int(input())

a = list(map(int,input().split()))
b = list(map(int,input().split()))

#a,b 각각 정렬
a.sort()
b.sort()

min_val = 0

for i in range(n):
    min_val += a[i] * b[n - 1 - i]     

print(min_val)