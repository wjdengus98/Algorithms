def solution(survey, choices):
    scores = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0,'A':0, 'N':0}
    answer = ""
    for i in range(len(survey)):
        word1 = survey[i][0]
        word2 = survey[i][1]
        
        if choices[i] in [1,2,3]:
            scores[survey[i][0]] += abs(choices[i] - 4)
        if choices[i] == 4:
            continue
        if choices[i] in [5,6,7]:
            scores[survey[i][1]] += abs(choices[i] - 4)
        
    # R과 T 비교
    if scores['R'] >= scores['T']:
        answer += 'R'
    else:
        answer += 'T'
    
     # C과 F 비교
    if scores['C'] >= scores['F']:
        answer += 'C'
    else:
        answer += 'F'
  
     # J과 M 비교
    if scores['J'] >= scores['M']:
        answer += 'J'
    else:
        answer += 'M'
        
     # A과 N 비교
    if scores['A'] >= scores['N']:
        answer += 'A'
    else:
        answer += 'N'
   
    return answer
    
