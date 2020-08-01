def solution(bridge_length, weight, truck_weights):
    bridge, day = [0]*bridge_length, 1
    bridge[0] = truck_weights.pop(0)
    while sum(bridge) != 0:
        if sum(bridge)+ truck_weights[0] <= weight and len(truck_weights) != 0:
            bridge = [truck_weights.pop(0)]+ bridge[:-1]
        else: bridge = [0] + bridge[:-1]
        day += 1
    return day
        
