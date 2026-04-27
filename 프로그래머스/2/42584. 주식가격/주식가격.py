def solution(prices):
    stack = []
    result = [0] * len(prices)
    
    for i in range(len(prices)):
        while stack and prices[stack[-1]] > prices[i]: # 떨어지는 순간
            idx = stack.pop()
            result[idx] = i - idx
        stack.append(i)
    
    for i in stack:
        result[i] = len(prices) - 1 - i
    
    return result