from collections import deque

def solution(skill, skill_trees):
    answer = 0

    for trees in skill_trees:
        q_order = deque([s for s in skill])
        for tree in trees: 
            if tree in skill: # 스킬셋이 배워야 할 스킬셋에 있을 경우
                if q_order[0] == tree: # 순서가 맞을 때
                    q_order.popleft()
                else: # 순서가 안맞으면 
                    break  # 종료
            else: # 스킬트리의 스킬이 배워야 할 스킬이 없을 경우
                continue
        else: # break 없이 for문 종료 → 유효한 스킬트리
            answer += 1                  
    
    return answer