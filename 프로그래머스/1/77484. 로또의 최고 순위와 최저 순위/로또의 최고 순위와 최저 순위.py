def solution(lottos, win_nums):
    rank = {'6' : 1, '5':2, '4': 3, '3':4, '2':5, '1':6, '0':6}
    max_cnt,min_cnt = 0,0
    ans = []
    for i in range(6):
        if lottos[i] in win_nums:
            max_cnt += 1
            min_cnt += 1
        if lottos[i] == 0:
            max_cnt += 1
    ans.append(rank[str(max_cnt)])
    ans.append(rank[str(min_cnt)])
    
    return ans