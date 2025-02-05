#백준 - 통게학(2108)

import sys

n = int(sys.stdin.readline())  # 빠른 입력
num_list = [int(sys.stdin.readline()) for _ in range(n)]  # 리스트에 입력값 저장
cnt_max = 0 #최빈값의 빈도수
freq_arr = [0] * 8001 #최빈값을 저장할 배열
first = True #최빈값이 여러개일 때 첫번째 값인지 확인

num_list.sort() #정렬
    
avg = round(sum(num_list) / n) #평균
mid = num_list[n // 2] #중앙값

#최빈값
for i in num_list:
    freq_arr[i + 4000] += 1 #최빈값을 freq_arr에 저장

for i in range(8001): #최빈값을 찾는다
    if freq_arr[i] > cnt_max: #최빈값이 더 크면
        cnt_max = freq_arr[i] #최빈값을 갱신
        freq_idx = i - 4000 #최빈값의 인덱스를 저장
        first = True
    elif freq_arr[i] == cnt_max and first: #최빈값이 같고 첫번째 값이면
        freq_idx = i - 4000 #최빈값의 인덱스를 저장
        first = False

freq = freq_idx
range = max(num_list) - min(num_list) # 범위

print(avg)
print(mid)
print(freq)
print(range)
