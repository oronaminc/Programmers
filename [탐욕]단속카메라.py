def solution(routes):
    routes.sort(key=lambda x:x[1])
    answer, end_point = 1, routes[0][1]
    for start, end in routes:
        if end_point < start:
            end_point = end
            answer += 1
    return answer