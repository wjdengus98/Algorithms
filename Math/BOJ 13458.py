#BOJ 시험감독

n = int(input()) # 시험장의 개수

students = list(map(int, input().split())) # 각 시험장의 응시자 수
b,c = map(int,input().split()) # 총감독관, 부감독관이 시험장에서 감시할 수 있는 수

cnt = 0 # 감독관 수

for i in range(n):
    students[i] -= b
    cnt += 1
    if students[i] > 0:
        cnt += students[i] // c
        if students[i] % c > 0:
            cnt += 1

print(cnt)