#백준 안테나(18310)

# n = int(input())
# house = sorted(list(map(int,input().split())))
# dist = []

# for i in range(n):
#     sum = 0 #거리의 합
#     a = house[i] 
#     for j in range(n):
#         b = house[j]
#         sum += abs(a-b) #두 집 사이의 거리 저장
#     dist.append(sum)

# for i in range(len(dist)):
#     min_idx = dist.index(min(dist)) #최소값이 되는 인덱스 구하기

# print(house[min_idx])


#시간 초과 이유: 시간복잡도가 O(n^2) 제곱이라서 N이 200,000일 때 시간을 초과하게 됨
# --> 시간 단축을 위해서 중앙값 이용 ----> O(nlogn)
#---------------------------------------------------------------------



n = int(input())  # 집의 개수 입력
house = sorted(list(map(int, input().split())))  # 집의 위치 입력 후 정렬

# 중앙값에 해당하는 집의 위치 출력 --> 중앙값이 거리의 합을 최소화 하게 만든다
print(house[(n - 1) // 2])
