def solution(N, number):
    if N==number: return 1
    NUM_LIST = [{N}]
    for num in range(2,9):
        temp_set = {int(str(N)*num)}
        for idx in range(num//2):
            for item1 in NUM_LIST[idx]:
                for item2 in NUM_LIST[-1-idx]:
                    temp_set.add(item1+item2)
                    temp_set.add(item1-item2)
                    temp_set.add(item2-item1)
                    temp_set.add(item1*item2)
                    if item1!=0: temp_set.add(item2//item1)
                    if item2!=0: temp_set.add(item1//item2)
        if number in temp_set: return num
        NUM_LIST.append(temp_set)
    return -1