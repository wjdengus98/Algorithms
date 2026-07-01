from collections import deque

def solution(bridge_length, weight, truck_weights):
    q = deque()
    truck_weights = deque(truck_weights) # 7,4,5,6
    time = 0
    cur_weights = 0

    while q or truck_weights:
        time += 1
        
        if q and time - q[0][1] == bridge_length:
            out_truck = q.popleft()
            cur_weights -= out_truck[0]
        
        if truck_weights and len(q) < bridge_length and cur_weights + truck_weights[0] <= weight:
            new_truck = truck_weights.popleft()
            q.append((new_truck, time))
            cur_weights += new_truck
    
    return time
