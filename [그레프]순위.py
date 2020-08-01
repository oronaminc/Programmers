from collections import defaultdict
def solution(n, results):
    win_dict, lose_dict, answer = defaultdict(set), defaultdict(set), 0
    for win, lose in results:
        win_dict[win].add(lose)
        lose_dict[lose].add(win)
    for idx_key in win_dict:
        for key, val in win_dict.items():
            if idx_key in val : win_dict[key] |= win_dict[idx_key]
    for idx_key in lose_dict:
        for key, val in lose_dict.items():
            if idx_key in val : lose_dict[key] |= lose_dict[idx_key]
    for num in range(1,n+1):
        if len(win_dict[num])+len(lose_dict[num]) == n-1: answer += 1
    return answer


# 얜 아직 이해 안
from collections import defaultdict
def solution(n, results):
    answer = 0
    win, lose = defaultdict(set), defaultdict(set)
    for result in results:
            lose[result[1]].add(result[0])
            win[result[0]].add(result[1])

    for i in range(1, n + 1):
        for winner in lose[i]: win[winner].update(win[i])
        for loser in win[i]: lose[loser].update(lose[i])

    for i in range(1, n+1):
        if len(win[i]) + len(lose[i]) == n - 1: answer += 1
    return answer