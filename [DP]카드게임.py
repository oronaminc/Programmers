def solution(left, right):
    L = len(left)
    answer = [[0] * (L+1) for i in range(L+1)]
    for i in reversed(range(L)):
        for j in reversed(range(L)):
            if left[j] > right[i]: answer[i][j] = answer[i+1][j] + right[i]
            else: answer[i][j] = max(answer[i][j+1], answer[i+1][j+1])
    return answer[0][0]