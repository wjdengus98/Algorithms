# 백준 2018번
# 연속된 자연수의 합 구하기
# 아이디어: 투 포인터의 이동 원칙(합 < N => 마지막 인덱스 오른쪽, 합 > N => 첫번째 인덱스 오른쪽)

N = int(input())

start  = 1
count = 1
end  = 1
answer = 1

while (start <= N):
    if answer == N:
        count += 1
        end += 1
    
    elif answer < N:
        end += 1
        answer += end
        
    elif answer > N:
        start += 1
        answer -= (start - 1)

print(count)