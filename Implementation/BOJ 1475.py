# 백준 알고리즘 - 1475번
# 방 번호
# https://www.acmicpc.net/problem/1475

n = input()

array = [0] * 10 # 0 ~ 9번의 방 번호를 저장할 배열
for i in n:
    num = int(i)
    array[num] += 1

max_val = -1 # 최댓값을 저장할 변수
for i in range(10):
   if  i == 6 or i == 9: # 6과 9는 같은 방 번호로 취급
       continue
   else:
       if max_val < array[i]:
              max_val = array[i]

final_val = max(max_val, (array[6] + array[9] + 1) // 2) # 나머지 방 번호와 6과 9의 방 번호의 최대값값
print(final_val)