def solution(s):
    stack = []
    for i in range(len(s)):
        stack.append(s[i])
        
        if len(stack) > 1:
            if stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
    
    if len(stack) == 0:
        return 1
    else:
        return 0
    