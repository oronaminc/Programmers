def find_location(LIST):
    temp = []
    for idx, val in enumerate(LIST):
        if val==1: temp.append(idx)
    return temp
def solution(n, computers):
    LIST = [i for i in range(len(computers))]
    cnt = 0
    temp = []
    while LIST:
        if len(LIST) != 0:
            cnt += 1
            temp = find_location(computers[LIST.pop(0)])
        for idx in temp:
            if idx in LIST:
                LIST.pop(LIST.index(idx))
                for item in find_location(computers[idx]):
                    if item in LIST: temp.append(item)
            else: continue
    return cnt




def solution(n, computers):
    lst = []
    for i in range(n):
        lst.append({i})
    for n1 in range(0, n):
        for n2 in range(n1+1, n):
            if computers[n1][n2] == 1:
                #print(n1,n2,lst)
                for idx,st in enumerate(lst):
                    if n1 in lst[idx]:
                        idx1 = idx
                    if n2 in lst[idx]:
                        idx2 = idx
                if idx1 != idx2:
                    hap = lst[idx1] | lst[idx2]
                    #print('hap : ', hap)
                    lst.pop(max(idx2,idx1))
                    lst.pop(min(idx1,idx2))
                    lst.append(hap)
        #print('lst : ', lst)
    return len(lst)


def solution2(n, computers):
    answer = 0
    visited = [0 for i in range(n)]
    def dfs(computers, visited, start):
        stack = [start]
        while stack:
            j = stack.pop()
            if visited[j] == 0:
                visited[j] = 1
            # for i in range(len(computers)-1, -1, -1):
            for i in range(0, len(computers)):
                if computers[j][i] ==1 and visited[i] == 0:
                    stack.append(i)
    i=0
    while 0 in visited:
        if visited[i] ==0:
            dfs(computers, visited, i)
            answer +=1
        i+=1
    return answer