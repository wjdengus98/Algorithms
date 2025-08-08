#1254번 펠린드롬 만들기
string = input()

if string == string[::-1]: #이미 펠린드롬이면
    print(len(string)) # 그대로 출력
else: #펠린드롬이 애초에 아니면
    
    for i in range(len(string)): #문자열의 길이까지를
        
        new_string = string + string[:i][::-1] #역순으로 채워서 더함
        
        if new_string == new_string[::-1]: #만약 펠린드롬이면
            print(len(new_string)) #그대로 출력
            break
