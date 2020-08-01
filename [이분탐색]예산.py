def solution(budgets, M):
    budgets.sort()
    L, answer = len(budgets), 0
    for idx, budget in enumerate(budgets):
        temp = (budget - answer) * (L-idx)
        if temp <= M:
            answer = budget
            M -= temp
        else:
            answer += M // (L - idx)
            break
    return answer

# sum 값이 커질수록 무조건 int overflow 남 => M에서 빼는 식으로 해야함
def solution(budgets, M):
    budgets.sort()
    if budgets[0]*len(budgets) > M: return M//len(budgets)
    elif sum(budgets) <= M: return budgets[-1]
    MIN,MAX, min_set = budgets[0], budgets[-1], set()
    while MAX-MIN>1:
        MID = (MIN+MAX)//2
        temp = [num if num <= MID else MID for num in budgets]
        if sum(temp) < M:
            MIN=MID
            min_set.add(MID)
        elif sum(temp) > M : MAX=MID-1
        else: return MID
    return max(min_set) if len(min_set) !=0 else MIN