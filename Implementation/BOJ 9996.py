# 백준 알고리즘 - 9996번
# https://www.acmicpc.net/problem/9996
# startswith, endswith를 이용하여 비교한다

n = int(input()) # 테스트 케이스 개수

pattern = input().split("*") # *을 기준으로 나눔

for _ in range(n):
    word = input() # 비교할 문자열 
    
    if (len(word) < len(pattern[0]) + len(pattern[1])): # 길이가 짧으면
        print("NE") # NO
        continue
    
    if (len(word) >= 1 and word.startswith(pattern[0]) and word.endswith(pattern[1])): # 시작과 끝이 맞으면
        print("DA") # YES
    else: # 아니면
        print("NE") # NO
    