def solution(n, times):
    times.sort()
    low, high = times[0] * n//len(times), times[-1] * n//len(times)
    while low < high:
        mid = (low+high)//2
        temp = 0
        for t in times: temp += (mid//t)
        if temp < n: low = mid + 1
        else: high = mid
    return low
    
import numpy as np
def solution(n, times):
    times.sort()
    low, high = times[0] * n//len(times), times[-1] * n//len(times)
    while low < high:
        mid = (low+high)//2
        temp = np.sum((np.zeros(len(times))+mid)//np.array(times))
        if temp < n: low = mid + 1
        else: high = mid       
    return low