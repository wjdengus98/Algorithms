def solution(wallet, bill):
    answer = 0
    while True:
        w = sorted(wallet)
        b = sorted(bill)

        if b[0] <= w[0] and b[1] <= w[1]:
            break

        if bill[0] >= bill[1]:
            bill[0] //= 2
        else:
            bill[1] //= 2

        answer += 1
    return answer