#백준 복호화

n = int(input())

for _ in range(n):
    line = input()
    frequency = [0] * 26 # 알파벳 빈도수
    
    for char in line: # 알파벳 빈도수 계산
        if char.isalpha(): # 알파벳인 경우
            frequency[ord(char) - ord('a')] += 1 # 알파벳 빈도수 증가
    
    max_freq = max(frequency) #가장 많이 나온 문자의 빈도수
    max_char = chr(frequency.index(max_freq) + ord('a')) #가장 많이 나온 문자
    
    if frequency.count(max_freq) > 1:
        print('?')
    else:
        print(max_char)
    

    