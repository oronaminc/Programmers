def solution(answers):
    L,a,b,c,a_C,b_C,c_C, answer = len(answers), [1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5], 0,0,0, []
    a_L, b_L, c_L = L//len(a)+1, L//len(b)+1, L//len(c)+1
    a, b, c = a*a_L, b*b_L, c*c_L
    for x,y,z,w in zip(answers,a,b,c):
        if x == y: a_C += 1
        if x == z: b_C += 1
        if x == w: c_C += 1
    max_num = max([a_C, b_C, c_C])
    for idx, num in enumerate([a_C, b_C, c_C]):
        if num == max_num: answer.append(idx+1)
    return answer
        
    