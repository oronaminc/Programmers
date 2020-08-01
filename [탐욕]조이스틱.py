def solution(name):
    char_list, idx = [min(ord(ch)-ord('A'), ord('Z')-ord(ch)+1) for ch in name], 0
    answer, char_list[0] = char_list[0], 0
    while sum(char_list) > 0:
        left, right = 1, 1
        while char_list[idx+right] <= 0: right +=1
        while char_list[idx-left] <= 0: left +=1
        answer += left if left<right else right
        idx += -left if left<right else right
        answer += char_list[idx]
        char_list[idx] = 0
    return answer

# 이거 11번 안됨 ㅠㅠ
def char_val(chracter):
    for i in range(14):
        if ord('A')+i == ord(chracter) or ord('Z')-(i-1) == ord(chracter): return i

def solution(name):
    answer, idx_set, idx = char_val(name[0]), set(), 0
    for item_idx, item in enumerate(name):
        if item_idx == 0: continue
        if item != 'A': idx_set.add(item_idx)

    while idx_set:
        for temp in range(1,(len(name)+1)//2+1):
            left_idx = idx-temp if idx-temp>0 else len(name)-1
            right_idx = idx+temp if idx+temp<len(name) else 0
            if right_idx in idx_set and left_idx in idx_set:
                idx = right_idx if char_val(name[right_idx]) >= char_val(name[left_idx]) else left_idx
                idx_set.remove(idx)
                answer += temp
                break
            elif right_idx in idx_set:
                idx = right_idx
                idx_set.remove(idx)
                answer += temp
                break
            elif left_idx in idx_set:
                idx = left_idx
                idx_set.remove(idx)
                answer += temp
                break
        answer += char_val(name[idx])
    return answer