def solution(arrangement):
    STICK, answer = 0, 0
    for idx, item in enumerate(arrangement):
        if item == "(":
            if arrangement[idx+1] == ")": answer += STICK
            else: STICK += 1
        else:
            if arrangement[idx-1] != "(": answer, STICK = answer +1, STICK-1
    return answer