def solution(data, ext, val_ext, sort_by):
    answer = []
    
    index_map = {
    "code": 0,
    "date": 1,
    "maximum": 2,
    "remain": 3
}
    
    ext_index = index_map[ext]  # 필터링 기준 인덱스
    sort_index = index_map[sort_by]  # 정렬 기준 인덱스
    
    
     #조건에 맞는 데이터 필터링
    answer = [item for item in data if item[ext_index] < val_ext]
    
    #데이터 값을 기준으로 오름차순으로 정렬
    answer.sort(key=lambda data: data[sort_index])
    return answer