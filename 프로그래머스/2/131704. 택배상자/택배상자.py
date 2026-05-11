def solution(order):
    n = len(order)
    cnt = 0
    belt = []

    for i in range(1, n+1):
        belt.append(i)

        while belt and belt[-1] == order[cnt]:
            belt.pop()
            cnt += 1
    return cnt


