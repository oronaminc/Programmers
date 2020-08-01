def solution(K, travel):
    Answer=[[0 for i in range(K+1)] for j in range(len(travel)+1)] 

    for i in range(1,len(travel)+1):
        [Wtime,Wmoney,Btime,Bmoney]=travel[i-1]
        for j in range(K+1):
            walk,bike=-1,-1
            if j>=Wtime and Answer[i-1][j-Wtime]!=-1: walk=Answer[i-1][j-Wtime]+Wmoney
            if j>=Btime and Answer[i-1][j-Btime]!=-1: bike=Answer[i-1][j-Btime]+Bmoney
            Answer[i][j]=max(walk,bike)

    return  Answer[len(travel)][K]


# 이건 시간 초과
def solution(K, travel):
    initial_list = [[K-travel[0][0], travel[0][1]],[K-travel[0][2], travel[0][3]]]
    for idx in range(1,len(travel)):
        walk_time, walk_cost, cycle_time, cycle_cost = travel[idx]
        temp_list = [[0,0] for i in range(2**(idx+1))]
        for temp_idx in range(len(temp_list)):
            if initial_list[temp_idx//2] == [0,0]:continue                
            if temp_idx%2 == 0:
                if initial_list[temp_idx//2][0]-walk_time<0: temp_list[temp_idx] = [0,0]
                else: temp_list[temp_idx] = [initial_list[temp_idx//2][0]-walk_time, initial_list[temp_idx//2][1]+walk_cost]
            else:
                if initial_list[temp_idx//2][0]-cycle_time<0: temp_list[temp_idx] = [0,0]
                else: temp_list[temp_idx] = [initial_list[temp_idx//2][0]-cycle_time, initial_list[temp_idx//2][1]+cycle_cost]
        initial_list = temp_list
    return(max(item[1] for item in initial_list))

# 이것도 시간초과
TRAVEL, K, MAX = [], 0, float('-inf')
def dfs(TIME, SUM, idx):
    global TRAVEL, K, MAX
    if TIME > K: return
    if len(TRAVEL) == idx:
        if MAX < SUM: MAX = SUM
        return
    dfs(TRAVEL[idx][0]+TIME, TRAVEL[idx][1]+SUM,idx+1)
    dfs(TRAVEL[idx][2]+TIME, TRAVEL[idx][3]+SUM,idx+1)

def solution(k, travel):
    global TRAVEL, K, MAX
    TRAVEL, K = travel, k
    dfs(0,0,0)
    return MAX