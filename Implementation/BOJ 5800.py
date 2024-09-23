#백준 5800 (성적 통계)

T = int(input())  # 반의 수 입력

for i in range(T):
    data = list(map(int, input().split()))  # 학생 수와 성적 데이터 입력
    N = data[0]  # 첫 번째 숫자는 학생 수
    scores = data[1:]  # 나머지는 성적 리스트

    print(f"Class {i+1}")
    
    scores.sort(reverse=True)  # 성적을 내림차순으로 정렬

    # 인접한 성적 차이를 계산하여 가장 큰 값 찾기
    gap_list = []
    for j in range(len(scores) - 1):
        gap_list.append(scores[j] - scores[j+1])

    # 최대 점수, 최소 점수, 가장 큰 인접한 점수 차이 출력
    print(f"Max {max(scores)}, Min {min(scores)}, Largest gap {max(gap_list)}")
