"""
큰 사각형의 넓이
= 갈색 격자의 개수(10) + 노란색 격자의 개수(2)
= 카펫의 가로(4) * 카펫의 높이(3)

작은 사각형의 넓이
= 노란색 격자의 개수 
= (카펫의 가로 - 2) * (카펫의 높이 - 2)
"""

def solution(brown, yellow):
    area = brown + yellow # 전체 카펫의 넓이: 갈색 + 노란색 격자의 수
    
    # height는 최소 3부터 시작 (테두리 최소 두 줄 필요)
    # 최대 area의 제곱근까지만 검사 (width와 height의 곱이 area이므로 대칭성 이용)
    for height in range(3, int(area**0.5) + 1):
        if area % height == 0: # area가 height로 나누어떨어지면 width를 구할 수 있음
            width = area // height
            if (width - 2) * (height - 2) == yellow: #노란색 영역의 넓이 구함
                return [width, height] #조건 만족시 가로, 높이 반환
  