import math

def solution(progresses, speeds):
    count = 0
    n = len(progresses)
    
    deployments = [math.ceil((100 - progresses[i]) / speeds[i]) for i in range(n)]
    
    max_deploy = deployments[0]
    
    answer = []
    for i in range(n):
        if deployments[i] <= max_deploy:
            count += 1
        else:
            answer.append(count)
            count = 1
            max_deploy = deployments[i]
    answer.append(count)
    
    return answer