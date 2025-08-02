from collections import Counter

string = input().strip() #주어진 문자 입력

counter = Counter(string) # Counter로 각 알파벳 개수 세기

odd_count = 0 # 홀수 문자 개수 

for c in counter.values():
    if c % 2 != 0: 
        odd_count += 1

    
if odd_count > 1: # 알파벳의 홀수 개수가 2개 이상이면
    print("I'm Sorry Hansoo") # 펠린드롬 못 만들음.
    exit()

half = ""
center = ""

for ch in sorted(counter.keys()): # 알파벳 순회하는 for문
    cnt = counter[ch] #각 알파벳의 개수
    if cnt % 2 != 0: #홀수이면
        center = ch #홀수 개수가 무조건 한개라면 가운데
    half += ch * (cnt // 2) # half에 차례대로 저장

result = half + center + half[::-1] # 대칭형 구조이니까 앞에 글자와 가운데 뒤집으면 펠린드롬 완성
print(result)
    