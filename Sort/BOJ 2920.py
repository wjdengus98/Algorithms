nums = list(map(int, input().split()))

if nums == sorted(nums):  # 원래 리스트와 오름차순 정렬된 리스트를 비교
    print('ascending')
elif nums == sorted(nums, reverse=True):  # 원래 리스트와 내림차순 정렬된 리스트를 비교
    print('descending')
else:
    print('mixed')