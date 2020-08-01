from heapq import *
def solution(scoville, K):
    heapify(scoville)
    if scoville[0] >=K: return 0
    cnt = 0
    while len(scoville) > 1:
        f,s = heappop(scoville), heappop(scoville)
        heappush(scoville, f+s*2)
        cnt += 1
        if scoville[0] >= K: return cnt
    return -1

# 최대 값이 었을 경우에 
for num in nums:
    heapq.heappush(heap, (-num, num)) 