def solution(n, costs):
    costs.sort(key=lambda x:x[2])
    point_set, answer = set(), costs[0][2]
    point_set.add(costs[0][0])
    point_set.add(costs[0][1])
    costs.pop(0)
    while n != len(point_set):
        idx = 0
        for start, end, value in costs:
            if start in point_set or end in point_set: 
                if not(start in point_set and end in point_set):
                    point_set.add(start)
                    point_set.add(end)
                    answer += value   
                costs.pop(idx)
                break
            idx += 1
    return answer