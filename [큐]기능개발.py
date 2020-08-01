def solution(progresses, speeds):
    done, idx, answer, cnt = [0]*len(progresses), range(0,len(progresses)), [], 1
    for i, p, s in zip(idx, progresses, speeds): done[i] = (100-p)//s if (100-p)%s==0 else (100-p)//s+1 
    standard = done[0]
    for idx in range(1, len(done)):        
        if done[idx] <= standard: cnt += 1
        else:
            standard = done[idx]
            answer.append(cnt)
            cnt = 1
    answer.append(cnt)
    return answer