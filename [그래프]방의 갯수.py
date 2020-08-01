def solution(arrows): #오일러의 다면체 정리(2차원): f = 1+e-v
    edge, vertex, x, y = set(), set(), 0, 0
    direction=[(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
    vertex.add((x,y))
    for dir_idx in arrows:
        for i in range(2):
            x2, y2 = direction[dir_idx][0]+x, direction[dir_idx][1]+y
            vertex.add((x2,y2))
            if (x,y) > (x2,y2): edge.add(((x,y), (x2,y2)))
            else: edge.add(((x2,y2), (x,y)))
            x,y = x2,y2
    return 1+len(edge)-len(vertex)