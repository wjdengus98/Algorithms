def solution(files):
    files_info = []

    for idx,file in enumerate(files):
        num_idx_list = [i for i in range(len(file)) if file[i].isnumeric()]
        first_idx = num_idx_list[0]
        last_idx = first_idx

        # 연속된 숫자로만 이루어진 부분을 찾기
        while last_idx < len(file) - 1 and file[last_idx + 1].isnumeric():
            last_idx += 1

        Head = file[0:first_idx].lower()
        Number = file[first_idx:last_idx + 1]
        Tail = file[last_idx+1:]

        files_info.append((Head, int(Number), idx, file))
        
    # 튜플 정렬하기 1차 사전순, 2차 숫자, 3번 idx 비교하기
    files_info.sort(key=lambda x: (x[0], x[1], x[2]))
    result = [info[3] for info in files_info]
    return result