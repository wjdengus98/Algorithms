#조교의 성적 매기기
T = int(input())

grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

for i in range(T):
     n,k = map(int,input().split())
     scores = []
     
     for j in range(n):
          mid,final,hw = map(int,input().split())
          total = (mid * 0.35) + (final * 0.45) + (hw * 0.2)
          scores.append(total)

     target = scores[k-1]

     sorted_scores = sorted(scores,reverse=True)
     
     grade_index = sorted_scores.index(target)

     rank = grade_index // (n // 10)

     print(f"#{i+1} {grades[rank]}")
          


          
