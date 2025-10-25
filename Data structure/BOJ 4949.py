# 백준 - 균형잡힌 세상
# 스택
while(True):
    stack = []
    flag = True
    
    s = input()
    
    if s == '.':
        break
    
    for char in s:
        if char in "([":
            stack.append(char)
        elif char == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                flag = False
                break
        elif char == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                flag = False
                break
    
    if flag and not stack:
        print("yes")
    else:
        print("no")
        