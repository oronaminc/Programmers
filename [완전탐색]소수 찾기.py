from itertools import permutations
import math
def is_Prime(num):
    if num < 2: return False
    for n in range(2, int(math.sqrt(num))+1):
        if num % n == 0: return False
    return True

def solution(numbers):
     num_list, L, num_set, cnt = str(' '.join(numbers)).split(' '), len(numbers), set(), 0
    num_list, L, num_set, cnt = [digit for digit in numbers], len(numbers), set(), 0
    for num in range(1,L+1): num_set.update(list(map(lambda x:int(''.join(x)), permutations(num_list, num))))
    for item in num_set:
        if is_Prime(item): cnt += 1
    return cnt
