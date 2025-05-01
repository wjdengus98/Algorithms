def solution(keymap, targets):
    min_pressed = {} #문자별 최소 누를 횟수 저장할 딕셔너리

    # keymap의 각 문자에 대해 최소 누를 횟수를 구한다.
    for i , key in enumerate(keymap):
        for idx, char in enumerate(key):
            if char in min_pressed:
                min_pressed[char] = min(min_pressed[char], idx + 1)
            else:
                min_pressed[char] = idx + 1

    result = [] # targets의 각 문자에 대해 최소 누를 횟수를 정할 리스트

    for target in targets:
        total = 0
        for char in target:
            if char in min_pressed:
                total += min_pressed[char]
            else:
                total = -1
                break
        result.append(total)


    return result