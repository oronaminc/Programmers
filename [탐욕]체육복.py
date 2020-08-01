def solution(n, lost, reserve):
    lost_set, reserve_list = set(lost)-set(reserve), sorted(set(reserve)-set(lost))
    for person in reserve_list:
        if person-1 in lost_set: lost_set.remove(person-1)
        elif person+1 in lost_set: lost_set.remove(person+1)
    return (n-len(lost_set))