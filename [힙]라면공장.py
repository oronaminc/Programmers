from heapq import *
def solution(stock, dates, supplies, k):
    HEAP, IDX, answer = [], 0, 0
    heapify(HEAP)
    while stock < k:
        for idx in range(IDX, len(dates)):
            if dates[idx] <= stock:
                heappush(HEAP, (-supplies[idx], supplies[idx]))
                IDX += 1
            else: break
        stock += heappop(HEAP)[1]
        answer += 1
    return answer
            
                