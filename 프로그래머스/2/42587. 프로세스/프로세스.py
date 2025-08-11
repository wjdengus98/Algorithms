from collections import deque

def solution(priorities, location):
    queue = deque()
    count = 0

    # 큐 초기화
    for idx, priority in enumerate(priorities):
        queue.append([idx, priority])

    while queue:
        process = queue.popleft()
        flag = False

        # 현재 process보다 높은 우선순위가 있는지 확인
        for other in queue:
            if process[1] < other[1]:
                flag = True
                break

        if flag:
            queue.append(process)  # 뒤로 보냄
        else:
            count += 1  # 실행 처리
            if process[0] == location:
                return count
