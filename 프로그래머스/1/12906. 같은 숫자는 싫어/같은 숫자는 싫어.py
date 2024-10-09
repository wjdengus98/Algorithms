def solution(arr):
    answer = []
    for i in arr:
        if len(answer) == 0: #스택이 비었다면
            answer.append(i) #우선 숫자를 넣는다
        else: #스택이 비지않았다면
            if answer[-1] == i:
                continue
            else:
                answer.append(i)
    return answer
