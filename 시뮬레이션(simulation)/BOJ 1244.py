# 백준
# 스위치 키고 끄기
# 시뮬레이션(구현)

t = int(input())

switches = list(map(int, input().split()))

s = int(input())

for i in range(s):
    sex, num = map(int, input().split())

    # 성별이 남자
    if sex == 1:
        n = len(switches) // num
        for j in range(1, n + 1):

            if switches[(num * j) - 1] == 0:
                switches[(num * j) - 1] = 1
            else:
                switches[(num * j) - 1] = 0
    # 성별이 여자
    elif sex == 2:
        # num번 스위치 자체 먼저 토글
        if switches[num - 1] == 0:
            switches[num - 1] = 1
        else:
            switches[num - 1] = 0
        
        left = num - 2  # 왼쪽 시작 인덱스
        right = num  # 오른쪽 시작 인덱스

        while left >= 0 and right < len(switches):
            if switches[left] == switches[right]:
                if switches[left] == 0:
                    switches[left] = 1
                    switches[right] = 1
                else:
                    switches[left] = 0
                    switches[right] = 0
                left -= 1
                right += 1
            else:
                break

# 한줄에 20개씩 출력
for i in range(0, t, 20):
    print(*switches[i:i+20])