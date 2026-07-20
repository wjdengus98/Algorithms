def solution(number, k):
    stack = []
    cnt = 0
    for i in range(len(number)):
        while stack and stack[-1] < number[i] and cnt < k:
            stack.pop()
            cnt += 1
        stack.append(number[i])
    if k - cnt > 0:
        stack = stack[:-(k - cnt)]
    else:
        pass
    return "".join(stack)

    