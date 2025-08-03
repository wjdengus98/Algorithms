def solution(s):
    #answer = True
    st = []
    for i in s:
        if i == '(':
            st.append(i)
        elif i == ')':
            if len(st) == 0:
                return False
            else:
                st.pop()
    
    if len(st) == 0:
        return True
    else:
        return False

