def solution(tickets):
    routes = dict()
    for (start, end) in tickets: routes[start] = routes.get(start, [])+[end]
    for key in routes.keys(): routes[key].sort()
    STACK, answer = ['ICN'], []
    while STACK:
        if STACK[-1] not in routes or len(routes[STACK[-1]])==0:answer.append(STACK.pop(-1))
        else:STACK.append(routes[STACK[-1]].pop(0))
    return answer[::-1]