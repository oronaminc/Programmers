def solution(people, limit):
    people.sort()
    answer, left_idx, right_idx = 0, 0, len(people)-1
    while right_idx-left_idx>=0:
        if people[left_idx] + people[right_idx] <= limit:
            left_idx += 1
            right_idx -=1
        else: right_idx -=1
        answer += 1
    return answer