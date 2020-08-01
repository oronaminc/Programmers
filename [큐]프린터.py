def solution(priorities, location):
    LIST, MAX, answer = [0]*len(priorities), max(priorities), 1
    for idx, value in enumerate(priorities): LIST[idx] = [idx, value]
    # LIST = [(i,p) for i,p in enumerate(priorities)]
    while LIST[0][0]!=location or LIST[0][1]!=MAX:
        if priorities[0] == MAX:
            LIST.pop(0)
            priorities.pop(0)
            answer += 1
            MAX = max(priorities)
        else:
            LIST.append(LIST.pop(0))
            priorities.append(priorities.pop(0))
    return answer