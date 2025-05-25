def solution(numbers, hand):
    answer = ''
    
    keypad = {
     1: (0, 0), 2: (0, 1), 3: (0, 2),
    4: (1, 0), 5: (1, 1), 6: (1, 2),
    7: (2, 0), 8: (2, 1), 9: (2, 2),
    '*': (3, 0), 0: (3, 1), '#': (3, 2)
}
    
    left_hand = keypad['*']
    right_hand = keypad['#']
    
    for i in range(len(numbers)):
        if numbers[i] in [1,4,7]: # 1,4,7번은 왼손으로 누르기
            answer += 'L'
            left_hand = keypad[numbers[i]] #왼손 위치 갱신
        elif numbers[i] in [3,6,9]: #3,6,9번은 오른손으로 누르기
            answer += 'R'
            right_hand = keypad[numbers[i]] #오른손 위치 갱신
        else: # 2,5,8,0번
            center = keypad[numbers[i]]
            left_dist = abs(left_hand[0] - center[0]) + abs(left_hand[1] - center[1]) 
            right_dist = abs(right_hand[0] - center[0]) + abs(right_hand[1] - center[1])

            if left_dist < right_dist: #왼손의 거리가 더 가까운 경우
                answer += 'L'
                left_hand = keypad[numbers[i]]
            elif left_dist > right_dist: #오른손의 거리가 더 가까운 경우
                answer += 'R'
                right_hand = keypad[numbers[i]]
            else: #왼손과 오른손이 누를 키패드와 거리가 같은 경우
                if hand == "right": #오른손잡이 -> 오른손으로 누르기기
                    answer += 'R'
                    right_hand = keypad[numbers[i]]
                else: #왼손잡이 -> 왼손으로 누르기
                    answer += 'L'
                    left_hand = keypad[numbers[i]]
    
    return answer