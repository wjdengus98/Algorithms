#파이썬 [S/W 문제해결 기본] - 숫자 카드

T= int(input())

for i in range(T):
    n = int(input())
    card = input()
    max_cnt = max_index = 0
    card_lists = [0] * 10

    #카드의 빈도 계산
    for c in card:
        c = int(c)
        card_lists[c] += 1        

        # 가장 많은 빈도를 가진 숫자 찾기(알고리즘 기억하기!)
        max_cnt = max(card_lists)
        for idx in range(10):
            if card_lists[idx] == max_cnt:
                max_index = idx

    print(f"#{i+1} {max_index} {max_cnt}")
    