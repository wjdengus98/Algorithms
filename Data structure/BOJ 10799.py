# 백준 10799번
# 쇠막대기
# https://www.acmicpc.net/problem/10799

s = input()
stack = []
cnt = 0

for i in range(len(s)):
    if s[i] == '(': #새로운 막대기 등장
        stack.append(s[i])
    else: # 닫힌 괄호가 나왔음
        if s[i - 1] == '(':
            stack.pop()
            cnt += len(stack)
        else: # 막대기가 끝났음
            stack.pop()
            cnt += 1

print(cnt)
            
        