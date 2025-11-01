# 백준 - 문자열 폭발
# 스택, 문자열

myStr = input().strip()
explosive_str = input().strip()

stack = []
m = len(explosive_str)

for i in range(len(myStr)):
    stack.append(myStr[i])
    
    if ''.join(stack[len(stack) - m : len(stack)]) == explosive_str: # 스택의 마지막 두 글자가 폭발 문자열과 같다면
        for _ in range(m): # 폭발 문자열 개수만큼
            stack.pop() # 문자 삭제
    
if stack:
    print(''.join(stack))
else:
    print("FRULA")

