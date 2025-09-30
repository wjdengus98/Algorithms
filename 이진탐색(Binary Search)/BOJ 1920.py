# 백준 알고리즘
# 수 찾기 - 이진탐색 알고리즘

def Bsearch(nums, v):
    first = 0
    last = len(nums) - 1
    
    while first <= last:
        mid = (first + last) // 2
        
        if v == nums[mid]:
            return 1
        elif v < nums[mid]:
            last = mid - 1
        elif v > nums[mid]:
            first = mid + 1
    return 0
        

n = int(input())
lst1 = list(map(int,input().split()))
lst1.sort()

m = int(input())
lst2 = list(map(int,input().split()))

res = []

for i in range(m):
    val = Bsearch(lst1,lst2[i])
    res.append(val)
    
for r in res:
    print(r)