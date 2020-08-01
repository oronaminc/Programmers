def solution(heights):
    heights_reverse, L, answer = heights[::-1], len(heights), []
    for std_idx, standard in enumerate(heights_reverse):
        CHANGE_FLAG = False
        for idx in range(std_idx+1, L):
            if heights_reverse[std_idx] < heights_reverse[idx]:
                answer.append(L-idx)
                CHANGE_FLAG = True
                break
        if not CHANGE_FLAG: answer.append(0)
    return answer[::-1]
        

def solution(heights):
    heights_reverse, L, answer = heights[::-1], len(heights), [0]*len(heights)
    for std_idx, standard in enumerate(heights_reverse):
        for idx in range(std_idx+1, L):
            if heights_reverse[std_idx] < heights_reverse[idx]:
                answer[std_idx] = (L-idx)
                break
    return answer[::-1]