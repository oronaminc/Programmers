#이게 리얼임
from heapq import *
def solution(jobs):
    jobs.sort()
    initial_time, end_time, answer, L, cnt, HEAP = -1, jobs[0][0], 0, len(jobs), 0, []
    while cnt<L:
        for start_time, during_time in jobs:
            if initial_time < start_time <= end_time:
                answer += (end_time-start_time)
                heappush(HEAP, during_time)
        if len(HEAP) != 0:
            initial_time = end_time
            end_time += HEAP[0]
            answer += len(HEAP)*heappop(HEAP)
            cnt +=1
        else: end_time += 1
    return answer//L

import heapq
def solution(jobs):
    start, end, L, count, answer, queue = -1, 0, len(jobs), 0, 0, []
    while count < L:
        for (start_time, during_time) in jobs:
            if start < start_time <= end:
                answer += (end-start_time)
                heapq.heappush(queue, during_time)
        if len(queue) > 0:
            answer += len(queue) * queue[0]
            start = end
            end += heapq.heappop(queue)
            count += 1
        else: end += 1
    return (answer//L)




from heapq import *
def solution(jobs):
    jobs.sort()
    time, answer, L = jobs[0][0], 0, len(jobs)
    while jobs:
        HEAP = []
        heapify(HEAP)
        for start_time, during_time in jobs:
            if start_time <= time: heappush(HEAP, (during_time, start_time))
            else: break
        if len(HEAP) != 0:
            during_time, start_time = heappop(HEAP)
            jobs.remove([start_time, during_time])        
            answer += (during_time+time-start_time)
            time += (during_time)
        else: time += 1
    return answer//L
    
        
        
from heapq import *
def solution(jobs):
    jobs.sort()
    time, answer, L, cnt = jobs[0][0], 0, len(jobs), 0
    HEAP = []
    heapify(HEAP)
    while jobs:
        for start_time, during_time in jobs:
            if start_time <= time and (during_time, start_time) not in HEAP: heappush(HEAP, (during_time, start_time))
        if len(HEAP) != 0:
            during_time, start_time = heappop(HEAP)
            jobs.remove([start_time, during_time])        
            answer += (during_time+time-start_time)
            time += (during_time)
        else: time += 1
    return answer//L
    