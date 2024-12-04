#[S/W 문제해결 기본] 1일차 - 최빈수 구하기

t= int(input())

for i in range(t):
    arr = [0] * 101
    test_num = int(input())
    scores = list(map(int, input().split()))
    scores.sort()
    max_idx = 0
    max_num = 0
    max_list = []
    for score in scores:
        arr[score] += 1

        if max_idx <= arr[score]:
            max_idx = arr[score]
            max_num = score      
            
    print(f"#{i + 1} {max_num}")