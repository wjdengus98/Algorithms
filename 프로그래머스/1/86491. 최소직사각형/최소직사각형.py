def solution(sizes):
    row = []
    col = []
    for i in range(len(sizes)):
        # 세로가 가로보다 크면 가로와 세로를 교환하여 가로가 항상 크도록 설정
        if sizes[i][0] < sizes[i][1]:
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]
        row.append(sizes[i][0])
        col.append(sizes[i][1])
        
    answer = max(row) * max(col) #명함을 모두 담을 수 있는 지갑크기는 가로와 세로의 최대값의 곱
    return answer