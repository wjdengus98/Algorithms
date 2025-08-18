def solution(arr1, arr2):
    answer = []
    l1, l2, l3 = len(arr1), len(arr1[0]), len(arr2[0])
    
    for i in range(l1):
        arr = arr1[i]
        res = []
        for j in range(l3):
            gop = 0
            for k in range(l2):
               gop += arr[k] * arr2[k][j]
            res.append(gop)
        answer.append(res)
    return answer