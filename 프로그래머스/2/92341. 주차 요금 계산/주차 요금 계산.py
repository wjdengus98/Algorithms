# 프로그래머스 주차 요금 계산

import math

def solution(fees, records):
    basic_time, basic_fee, unit_time,unit_fee = fees[0], fees[1], fees[2],fees[3]
    
    in_time = {} # 차번호: 현재 IN 시간
    total_time = {} #차번호: 누적 주차 시간
    for record in records:
        time, car_num, status = record.split()
        h,m = time.split(":")
        total_min = int(h) * 60 + int(m)
        print(f"시간 변환:{total_min}")
        if status == "IN":
            in_time[car_num] = total_min
            print(f"출차 시간: {in_time[car_num]}")
        else:
            out_time = total_min
            total_time[car_num] = total_time.get(car_num,0) + out_time - in_time[car_num]
            print(f"나간 시간: {total_time[car_num]}")
            del in_time[car_num]
    
    for car_num in in_time:
        total_time[car_num] = total_time.get(car_num, 0) + 1439 - in_time[car_num]
    
    sorted_total_time = sorted(total_time.items())
    prices_list = []
    for car_num, park_time in sorted_total_time:
        if park_time <= basic_time:
            price = basic_fee
        else:
            price = basic_fee + math.ceil((park_time - basic_time) / unit_time) * unit_fee
        
        prices_list.append(price)
    return prices_list