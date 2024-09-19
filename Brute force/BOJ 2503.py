n = int(input())

hint = [list(map(int, input().split())) for _ in range(n)]

answer = 0

# 1부터 9까지의 숫자 중 서로 다른 숫자로 이루어진 세 자리 수를 순회
for x in range(1, 10):
    for y in range(1, 10):
        for z in range(1, 10):
            if x == y or y == z or z == x:
                continue  # 중복되는 숫자는 제외

            # 숫자가 정해짐
            cnt = 0
            for arr in hint:
                number = str(arr[0])  # 민혁이가 질문한 숫자
                strike = arr[1]
                ball = arr[2]

                # x, y, z (후보 숫자)와 number (민혁이가 질문한 숫자)를 비교하여 스트라이크와 볼을 계산
                strike_cnt = 0
                ball_cnt = 0

                # 스트라이크 계산
                if x == int(number[0]):
                    strike_cnt += 1
                if y == int(number[1]):
                    strike_cnt += 1
                if z == int(number[2]):
                    strike_cnt += 1

                # 볼 계산 (스트라이크는 제외하고 볼 계산)
                if x in map(int, number) and x != int(number[0]):
                    ball_cnt += 1
                if y in map(int, number) and y != int(number[1]):
                    ball_cnt += 1
                if z in map(int, number) and z != int(number[2]):
                    ball_cnt += 1


                # 스트라이크와 볼이 맞는지 확인
                if strike_cnt == strike and ball_cnt == ball:
                    
                    cnt += 1

            # 모든 힌트에 대해 일치하면 가능한 답
            if cnt == n:
                answer += 1

print(answer)

