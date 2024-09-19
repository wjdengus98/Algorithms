#백준: 나는 요리사다

cookers = []

for i in range(5):
    a = map(int, input().split())
    cookers.append(sum(a))

# 가장 높은 점수를 찾기 위해 max를 사용합니다.
max_score = max(cookers)
winner_index = cookers.index(max_score) + 1  # 참가자 번호는 1부터 시작하므로 +1

print(winner_index, max_score)


