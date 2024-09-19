#백준 10867

# 입력 받기
n = int(input())  # 수의 개수 n
nums = list(map(int, input().split()))  # N개의 정수 입력받기

# 중복을 제거하고 정렬
unique_nums = sorted(set(nums))

# 결과 출력
print(" ".join(map(str, unique_nums)))