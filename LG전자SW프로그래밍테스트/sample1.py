# LG전자SW프로그래밍테스트 - SAMPLE 1
# 산책

N,T = map(int,input().split())
predict = []
for i in range(N):
    p,s = map(int,input().split())
    
    location = p + (s*T)
    predict.append(location)


for i in range(len(predict) - 1 , 0, -1):
    if predict[i-1] >= predict[i]: # 뒷 사람 직원 위치가 앞 사람 위치보다 크면
        predict[i-1] = predict[i]  # 앞 사람 위치로 바꾼다.

real_predict = set(predict) # 그룹셋 형성
print(len(real_predict))    