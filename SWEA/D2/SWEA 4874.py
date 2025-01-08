# SWEA [파이썬 문제해결 기본]5일차 - Forth

TC = int(input())

for i in range(TC):
    stack = []
    string = input().split()
    error = False
    
    for s in string:
        if s.isdigit(): # 숫자인 경우
            stack.append(int(s))
        elif s in ['+', '-', '*', '/']: # 연산자인 경우
            if len(stack) < 2: # 스택에 숫자가 두 개 미만인 경우
                print(f'#{i + 1} error')
                error = True
                break
            b = stack.pop()
            a = stack.pop()
            if s == '+':
                stack.append(a + b)
            elif s == '-':
                stack.append(a - b)
            elif s == '*':
                stack.append(a * b)
            elif s == '/':
                stack.append(a // b)
                
        elif s == '.': # 마침표인 경우
            break
        else: # 숫자나 연산자가 아닌 경우
            print(f'#{i + 1} error')
            error = True
            break
        
    if not error:
        if len(stack) == 1: # 에러가 없고 스택에 숫자가 하나만 남은 경우
            print(f'#{i + 1} {stack[0]}')
        else: #스택에 숫자가 하나만 남지 않은 경우
            print(f'#{i + 1} error')
    
    
        
    