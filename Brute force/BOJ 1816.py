# BOJ 1816 암호키

# 100만 작고 2이상의 약수를 가지고 있다면, 틀린 비밀번호!

TC = int(input())

for _ in range(TC):
    num = int(input())

    for i in range(2, 1_000_001):
        if num % i == 0: #100만 이하 약수가 존재한다!
            print("NO")
            break
        if i == 1_000_000: #100만 이하의 약수가 존재하지 않는다!
            print("YES")