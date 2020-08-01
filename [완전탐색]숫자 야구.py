from itertools import permutations
def solution(baseball):
    num_set= set(permutations(range(1,10), 3))
    for num, strike, ball in baseball:
        result_set = set()
        for x,y,z in num_set:
            temp_strike, temp_ball = 0, 0
            if str(num)[0] == str(x): temp_strike += 1
            if str(num)[1] == str(y): temp_strike += 1
            if str(num)[2] == str(z): temp_strike += 1
            if str(x) in str(num) and str(x)!=str(num)[0]: temp_ball += 1
            if str(y) in str(num) and str(y)!=str(num)[1]: temp_ball += 1
            if str(z) in str(num) and str(z)!=str(num)[2]: temp_ball += 1
            if temp_ball == ball and temp_strike == strike: 
                result_set.add((x,y,z))
        print(result_set, '\n')
        num_set = result_set
        # print(num_set, '\n')
    
baseball = [[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]
solution(baseball)