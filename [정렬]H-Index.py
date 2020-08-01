def solution(citations):
    citations.sort(reverse=True)
    for idx in range(len(citations)-1, -1, -1):
        if citations[idx] >= idx+1: return idx+1
    return 0
        