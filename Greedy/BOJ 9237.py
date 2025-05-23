n = int(input())
trees = list(map(int,input().split()))
trees.sort(reverse=True)

max_day = 0
for i in range(len(trees)):
    grow_day = i + trees[i] + 1
    if grow_day > max_day:
        max_day = grow_day

print(max_day + 1)  # 마지막 나무 자란 다음 날이 파티 날
