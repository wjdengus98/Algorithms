#SWEA 6730. 장애물 경주 난이도

TC = int(input()) #테스트 케이스 개수 입력

for test_case in range(TC):
    N = int(input())
    arr = list(map(int, input().split()))
    
    # 올라가기와 내려가기 높이 차이를 저장할 리스트 초기화
    climb = []
    down = []
    
    # 블록 높이 배열을 순회하며 높이 차이 계산
    for i in range(N - 1):
        result = arr[i] - arr[i + 1]
        
        if result > 0: #높이 차이가 양수면
            down.append(abs(result)) #내려가기 리스트 저장장
        else: # 음수이면면
            climb.append(abs(result)) #올라가기 리스트 저장
    
    # climb이나 down이 비어 있는 경우 0을 추가
    if not climb or not down:
        climb.append(0) if not climb else down.append(0)

    print(f'#{test_case + 1} {max(climb)} {max(down)}')
    