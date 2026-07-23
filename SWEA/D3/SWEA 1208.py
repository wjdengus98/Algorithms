# [S/W 문제해결 기본] - Flatten

for i in range(10):
    dump = int(input()) # dump 가능 횟수
    boxes = list(map(int,input().split())) # 상자 배열
    
    for _ in range(dump):
        maxval = max(boxes) #최대값
        minval = min(boxes) #최소값
        maxidx = boxes.index(maxval) # 최대값 인덱스
        minidx = boxes.index(minval) # 최소값 인덱스
        boxes[maxidx] -= 1 # 큰 값에서 1 빼기
        boxes[minidx] += 1 # 가장 작은 값에서 1 더하기
    answer = max(boxes) - min(boxes) # 최대 최소 차
    print(f"#{i+1} {answer}")