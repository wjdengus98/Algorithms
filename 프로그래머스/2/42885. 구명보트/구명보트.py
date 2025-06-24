def solution(people, limit):
    # 투포인트 이용하기
    # 가벼운 사람과 무거운 사람을 먼저 태우기!
    people.sort()
    left = 0 #가장 가벼운 사람
    right = len(people) - 1 # 가장 무거운 사람
    boat = 0
    
    while left <= right:
        if people[left] + people[right] <= limit: #둘 다 탑승 할 수 있으면
            left += 1 #가벼운 사람도 탑승
        right -= 1 #무거운 사람은 항상 탑승
        boat += 1
    
    return boat