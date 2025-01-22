def solution(answers):
    #수포자들의 답안 패턴
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    scores = [0,0,0] #각 수포자들의 점수 저장 리스트
    
    # 답안과 비교하며 수포자의 점수 비교
    for i in range(len(answers)):
        if answers[i] == a[i%len(a)]:
            scores[0] += 1
        if answers[i] == b[i%len(b)]:
            scores[1] += 1
        if answers[i] == c[i%len(c)]:
            scores[2] += 1
    
    #가장 높은 점수 찾기
    max_score = max(scores)
    
    #최대 점수 맞은 학생 모두 찾기
    result = [i+1 for i in range(3) if scores[i] == max_score]
    
    return result
        
    
 