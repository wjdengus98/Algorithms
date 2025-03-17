# 백준 알고리즘 - 20291번
# 파일 정리

n = int(input()) # 파일의 개수

file = {} # 파일의 확장자를 저장할 딕셔너리

for _ in range(n):
    s = input().split('.')[1] # '.'을 기준으로 파일이름, 확장자 구분
    if s in file: # 딕셔너리에 확장자가 존재하면
        file[s] += 1 # 해당 확장자의 개수를 1 증가
    else: # 딕셔너리에 확장자가 존재하지 않으면
        file[s] = 1 # 확장자를 파일에 넣고 개수를 1로 초기화

file = sorted(file.items()) # 딕셔너리를 키를 기준으로 오름차순

for i in file: # key, value 출력
    print(i[0], i[1])