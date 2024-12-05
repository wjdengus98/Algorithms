#9012 괄호
t = int(input())

for i in range(t):
    stack = []
    bracket = input()
    flag = True
    
    for b in bracket:
        if b == "(": # (이면 우선 스택에 넣는다
            stack.append(b)
        elif b == ")":
            if len(stack) == 0: #스택이 비어 있으면 
                print("NO") #유효하지 않다
                flag = False
                break
            else: 
                stack.pop() #스택의 마지막 괄호 제거
    if flag:
        if len(stack) == 0:
            print("YES")
        else:
            print("NO")