def solution(s):
    n = len(s)
    cnt = 0
    for i in range(n):
        stack = []
        is_valid = True
        for j in range(n):
            c = s[(i+j) % n]
            
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            else:
                if not stack:
                    is_valid = False
                    break
            
                top = stack.pop()
            
            if c == ")" and top != '(':
                is_valid = False
                break
            if c == ']' and top != '[':
                is_valid = False
                break
            if c == '}' and top != '{':
                is_valid = False
                break
            
        if is_valid and not stack:
            cnt += 1
            
    return cnt