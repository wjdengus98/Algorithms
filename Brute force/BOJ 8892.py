# 백준 알고리즘
# 8892번

def is_palindrome(s):
    return s == s[::-1]

T = int(input())

for i in range(T):
    k = int(input())
    word_list = []
    for j in range(k):
        word_list.append(input())
    flag = False
    
    word = ""
    
    for i in range(len(word_list)):
        for j in range(len(word_list)):
            if i != j:
                combined = word_list[i] + word_list[j]
                if is_palindrome(combined):
                    flag = True
                    word = combined
                    break
        if flag:
            break
        
        
    if flag:
        print(word)
    else:
        print(0)   
    
    
    