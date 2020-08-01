def solution(money):
    L = len(money)
    dp1, dp2 = [0]*L, [0]*L
    dp1[0], dp1[1] = money[0], max(money[0], money[1])
    dp2[0], dp2[1] = 0, money[1]
    for idx in range(2, L-1): dp1[idx] = max(dp1[idx-1], dp1[idx-2]+money[idx])
    for idx in range(2, L): dp2[idx] = max(dp2[idx-1], dp2[idx-2]+money[idx])
    return max(dp2[-1], dp1[-2])