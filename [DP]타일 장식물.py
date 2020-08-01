def solution(N):
    if N == 1: return 4
    fibo = [1,1] + [0]*(N-2)
    for idx in range(2,N): fibo[idx] = fibo[idx-1] + fibo[idx-2]
    return fibo[N-1]*4+fibo[N-2]*2