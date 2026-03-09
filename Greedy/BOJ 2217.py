# 백준 로프

n = int(input())

ropes = [int(input()) for _ in range(n)]

# 내림차순 정렬 => 강한 로프부터 사용
ropes.sort(reverse=True)

max_weight = 0

for i in range(n):
    rope = ropes[i] # 가장 강한 로프부터 사용(내림차순이므로)
    
    weight = rope * (i+1)
    
    # 지금까지의 최대 중량과 비교해서 갱신
    if weight > max_weight:
        max_weight = weight

print(max_weight)