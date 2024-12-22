def solution(array, commands):
    answer = []
    
    for i in range(len(commands)):
        arr = sorted(array[commands[i][0] - 1:commands[i][1]])
        find_val = arr[commands[i][2] -1]
        answer.append(find_val)
    return answer