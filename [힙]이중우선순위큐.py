from heapq import *
def solution(operations):
    HEAP, answer = [], [0,0]
    for item in operations:
        operator, digit = item.split(' ')
        digit = int(digit)
        if operator == "I": heappush(HEAP, digit)
        elif operator == "D" and len(HEAP) > 0:
            if digit == -1: heappop(HEAP)
            elif digit == 1:
                temp = []
                while len(HEAP) > 1: heappush(temp,heappop(HEAP))
                HEAP = temp
    if len(HEAP) == 0: return answer
    else:
        answer[1] = HEAP[0]
        while len(HEAP) > 1: heappop(HEAP)
        answer[0] = HEAP[0]
        return answer
    
from heapq import *
def solution(arguments):
    max_heap, min_heap = [], []
    for arg in arguments:
        if arg == "D 1":
            if max_heap != []:
                heappop(max_heap)
                if max_heap == [] or -max_heap[0] < min_heap[0]: max_heap, min_heap = [], []
        elif arg == "D -1":
            if min_heap != []:
                heappop(min_heap)
                if min_heap == [] or -max_heap[0] < min_heap[0]: max_heap, min_heap = [], []
        else:
            num = int(arg[2:])
            heappush(max_heap, -num)
            heappush(min_heap, num)
    if min_heap == []:return [0, 0]
    return [-heappop(max_heap), heappop(min_heap)]