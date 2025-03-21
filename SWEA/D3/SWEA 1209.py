# 1209. [S/W 문제해결 기본] 2일차 - Sum

T  = 10

for tc in range(1, T+1):
    t = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)] # 100*100 배열 입력받기
    
    ans = s3 = s4 = 0 # ans: 최대값, s3: 대각선1, s4: 대각선2
    for i in range(100):
        s1 = s2 = 0
        for j in range(100):
            s1 += arr[i][j] # 가로
            s2 += arr[j][i] # 세로
        ans = max(ans, s1, s2) # 최대값 갱신
        
        s3 += arr[i][i] # 대각선1
        s4 += arr[i][99 - i] # 대각선2
    ans = max(ans, s3, s4) # 최대값 갱신
    
    print(f'#{tc} {ans}')