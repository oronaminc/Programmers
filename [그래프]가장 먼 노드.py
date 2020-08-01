def solution(n, edge):
    edge_dict, range_set, temp_set = dict(), set(range(1,n+1)), {1}
    for num in range_set: edge_dict[num] = set()
    for pt1, pt2 in edge:
        edge_dict[pt1].add(pt2)
        edge_dict[pt2].add(pt1)
    range_set.remove(1)
    while range_set:
        temp_set2 = set()
        for node in temp_set:            
            for item in edge_dict[node]:
                if item in range_set:
                    temp_set2.add(item)
                    range_set.remove(item)
                    if len(range_set)==0: return len(temp_set2)
        if len(temp_set2)==0: return len(range_set)        
        temp_set = temp_set2