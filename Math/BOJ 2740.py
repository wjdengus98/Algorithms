#백준 2740번 행렬곱셈

n,m1 = map(int, input().split())

matrix1 = []
matrix2 = []

for _ in range(n):
    matrix1.append(list(map(int, input().split())))

m,k = map(int,input().split())

for _ in range(m):
    matrix2.append(list(map(int,input().split())))

matrix = []
for i in range(n):
    line = []
    for j in range(k):
        mul_val = 0
        for t in range(m):
            mul_val += matrix1[i][t] * matrix2[t][j]
        line.append(mul_val)
    matrix.append(line)

for i in matrix:
    print(*i)
