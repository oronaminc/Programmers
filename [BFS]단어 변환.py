def solution(begin,target,words):
    if target not in words: return 0
    begins, answer = [begin], 0
    while(words):
        for item_begin in begins:
            temp = []
            for item_word in words:
                diff_cnt = 0
                for idx in range(len(item_begin)):
                    if item_word[idx] != item_begin[idx]: diff_cnt +=1
                    if diff_cnt >= 2: break
                if diff_cnt==1:
                    temp.append(item_word)
                    words.remove(item_word)
        begins, answer = temp, answer+1
        if target in begins: return answer  
