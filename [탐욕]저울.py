def solution(weight):
    answer = 1
    for item in sorted(weight):
        if item > answer:break
        else: answer += item
    return answer