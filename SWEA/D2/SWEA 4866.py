#SWEA 4866 괄호검사

t = int(input())

for i in range(t):
    string = input()
    stack = []
    is_valid = True  # 괄호 검사 상태 플래그

    for char in string:
        if char == '(' or char == '{':
            stack.append(char)
        elif char == ')':
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                is_valid = False
                break
        elif char == '}':
            if stack and stack[-1] == "{":
                stack.pop()
            else:
                is_valid = False
                break

    # 스택이 비어있지 않거나 플래그가 False인 경우 실패
    if stack or not is_valid:
        print(f"#{i+1} 0")
    else:
        print(f"#{i+1} 1")
