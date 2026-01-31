def solution(name, yearning, photo):
    scores = []
    for i in range(len(photo)):
        for j in range(len(photo[i])):
            if photo[i][j] in name:
                idx = name.index(photo[i][j])
                photo[i][j] = yearning[idx]
            else:
                photo[i][j] = 0
    for i in range(len(photo)):
         scores.append(sum(photo[i]))
    
    return scores