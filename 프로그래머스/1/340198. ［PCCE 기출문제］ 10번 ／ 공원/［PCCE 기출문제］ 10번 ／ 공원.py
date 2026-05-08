def solution(mats,park):
    res = []
    
    for mat in mats:
        for i in range(len(park) - mat + 1):
            for j in range(len(park[i]) - mat + 1):
                
                can_place = True
                for k in range(mat):
                    for l in range(mat):
                        if  park[i + k][j + l] != '-1':
                            can_place = False
                            break
                    if not can_place:
                        break
            
                if can_place:
                    res.append(mat)
                    break

            if can_place:
                break    
    return max(res) if res else -1