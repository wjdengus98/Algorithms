#백준 좋은 단어(3986)

#스택을 사용하는 문제

n = int(input())

good_word = 0

for i in range(n):
    word = input()
    stack = []  # 스택을 각 단어마다 새로 초기화
    
    for j in word:
        if len(stack) == 0:  # 스택이 비었다면
            stack.append(j)  # 단어를 넣는다
        else:  # 스택이 비지 않고
            if stack[-1] == j:  # 스택 위에 있는 글자와 현재 글자가 같으면
                stack.pop()  # 원소를 제거
            else:  # 같지 않다면
                stack.append(j)  # 원소를 추가

    if len(stack) == 0:  # 스택이 비었으면 좋은 단어
        good_word += 1

print(good_word)


            
    

    


