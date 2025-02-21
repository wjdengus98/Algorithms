# 백준 알고리즘 - 25192번

n = int(input())

cnt = 0 #곰곰티콘을 셀 변수
gom = set() #곰곰티콘을 저장할 집합

for i in range(n):
    text = input()
    if text == "ENTER": #ENTER일 경우 집합에 추가
        cnt += len(gom) #곰곰티콘 개수 추가
        gom.clear() #곰곰티콘 비워줌
    else: # TEXT일 경우
        gom.add(text) # 집합에 추가
        
cnt += len(gom) # 마지막 ENTER가 없을 경우를 대비하여 추가
print(cnt)

  