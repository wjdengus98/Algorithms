#백준 비밀번호 발음하기
#https://www.acmicpc.net/problem/4659

while True:
    word = input()
    
    if word == 'end': #입력 종료 조건
        break
    
    vowels = ['a', 'e', 'i', 'o', 'u']
    has_vowel = False #모음 존재 여부
    has_double = False #연속된 문자 존재 여부
    invalid = False #유효성 여부
    consecutive_vowel = 0 #모음 연속 횟수
    consecutive_consonant = 0 #자음 연속 횟수
    prev = '' #이전 문자
    
    for c in word:
        if c in vowels:
            has_vowel = True
            consecutive_vowel += 1
            consecutive_consonant = 0
        else:
            consecutive_consonant += 1
            consecutive_vowel = 0
        
        #모음이 3번 연속되거나 자음이 3번 연속되면 유효하지 않음
        if consecutive_vowel == 3 or consecutive_consonant == 3:
            invalid = True
            break
        
        #연속된 문자가 존재하는지 확인
        if c == prev and c != 'e' and c != 'o':
            has_double = True
        
        prev = c
    
    if invalid or not has_vowel or has_double: #유효하지 않은 경우
        print('<' + word + '> is not acceptable.')
    else:
        print('<' + word + '> is acceptable.')
        
        
    