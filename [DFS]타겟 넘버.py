def solution(numbers, target):
    cnt, L = 0, len(numbers)
    def operator(idx):
        if idx < L:
            numbers[idx] *= 1
            operator(idx+1)
            numbers[idx] *= -1
            operator(idx+1)
        elif sum(numbers) == target:
            nonlocal cnt
            cnt += 1
    operator(0)
    return cnt



def solution(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])