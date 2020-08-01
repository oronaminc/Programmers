def solution(m, n, puddles):
    routes = [[0]*(m+1) for i in range(n+1)]
    for row in range(1, n+1):
        for col in range(1, m+1):
            if row == 1 and col ==1: routes[1][1] = 1
            elif [col,row] in puddles: routes[row][col] = 0
            else: routes[row][col] = routes[row][col-1] + routes[row-1][col]
    return routes[n][m]%1000000007