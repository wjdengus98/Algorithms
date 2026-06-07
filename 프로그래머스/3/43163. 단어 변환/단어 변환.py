from collections import deque

def solution(begin, target, words):
    
    if target not in words:
        return 0
    
    queue = deque()
    queue.append((begin, 0))
    visited = set()
    visited.add(begin)
    
    while queue:
        cur_word, cnt = queue.popleft()
        
        
        for word in words:
            count = 0
            for i in range(len(word)):
                if cur_word[i] != word[i]:
                    count += 1 # 딱 글자가 다를 때
            
            if count == 1 and word not in visited: # 한 글자만 다르고 방문 안했을 때
                if word == target:
                    return cnt + 1
                queue.append((word, cnt+1)) # 큐에 새로운 단어와 횟수 증가
                visited.add(word)
    return 0
