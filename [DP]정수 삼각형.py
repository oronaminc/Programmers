def solution(triangle):
    new_triangle = []
    for LIST in triangle: new_triangle.append([0] + LIST + [0])
    for list_idx in range(len(new_triangle)-1):
        for item_idx in range(1,len(new_triangle[list_idx+1])-1):
            new_triangle[list_idx+1][item_idx] = max(new_triangle[list_idx][item_idx], new_triangle[list_idx][item_idx-1]) + new_triangle[list_idx+1][item_idx]
    return max(new_triangle[-1])

def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(1, i):
            triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])
        triangle[i][0] += triangle[i-1][0]
        triangle[i][-1] += triangle[i-1][-1]
    answer = max(triangle[-1])
    return answer