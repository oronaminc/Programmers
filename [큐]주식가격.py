def solution(prices):
    answer = [0]*len(prices)
    for std_idx, standard in enumerate(prices):
        for idx in range(std_idx+1, len(prices)):
            if prices[idx] >= standard: answer[std_idx] += 1
            else:
                answer[std_idx] += 1
                break
    return answer
            