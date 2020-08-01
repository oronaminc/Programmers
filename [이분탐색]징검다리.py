def solution(distance, rocks, n):
    answer, sorted_rocks = 0, sorted(rocks+[distance])
    left,right = 0, distance
    while (left <= right):
        mid = (left + right) // 2
        cnt, p = 0, 0
        for i in range(len(sorted_rocks)):
            if (sorted_rocks[i] - p < mid): cnt += 1
            else: p = sorted_rocks[i]
        if cnt > n: right = mid - 1
        else:
            left = mid + 1
            answer = mid
    return answer
