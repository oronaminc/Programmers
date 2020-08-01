'''
def maxDifference(px):
    print(sorted(px, reverse=True))
    if px == sorted(px, reverse=True):return -1
    max_diff_set, MIN_IDX, MAX_IDX, MIN_FLAG, MAX_FLAG = set(), 0,0, False, False
    for idx in range(1,len(px)):
        if not MIN_FLAG:
            if px[idx-1] < px[idx]:
                MIN_FLAG = True
                MIN_IDX = idx-1
        if MIN_FLAG:
            if px[idx-1] >= px[idx]:
                MAX_FLAG = True
                MAX_IDX = idx-1
        if MIN_FLAG and MAX_FLAG:
            max_diff_set.add(px[MAX_IDX]-px[MIN_IDX])
            MIN_FLAG, MAX_FLAG = False, False
            MIN_IDX = idx
    if MIN_FLAG: max_diff_set.add(px[-1]-px[MIN_IDX])
    return max(max_diff_set)





def scatterPalindrome(strToEvaluate):
# Write your code here
   answer = []
   for item in strToEvaluate:
       cnt = 0        
       for start_idx in range(len(item)):
           temp_dict = dict()
           for idx in range(start_idx,len(item)):
               temp_dict[item[idx]] = temp_dict.get(item[idx],0) + 1
               isPalindrome, FLAG = 0, True
               for val in temp_dict.values():
                   if val%2==1:
                       isPalindrome += 1
                       if isPalindrome >= 2:
                           FLAG = False
                           break
               if FLAG: cnt+=1
       answer.append(cnt)
   return answer

def scatterPalindrome(strToEvaluate):
    # Write your code here
    answer = []
    for item in strToEvaluate:
        cnt = 0        
        for start_idx in range(len(item)):
            temp_dict, temp_set = dict(), set()
            for idx in range(start_idx,len(item)):
                if item[idx] not in temp_set: temp_set.add(item[idx])
                else: temp_set.remove(item[idx])
                if len(temp_set)<=1: cnt += 1
        answer.append(cnt)
    return answer
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import codecs
import random
sys.stdin = codecs.getreader("utf-8")(sys.stdin.detach())
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
num = int(input())
for i in range(num):
    playlist = sys.stdin.readline().replace('\n','').split('\t')
    artist = sys.stdin.readline().replace('\n','').split('\t')
    song_dict, suffle_list, shuffle_idx = dict(), [" "]*len(artist), list(range(len(artist)))
    for artist_item, playlist_item in zip(artist, playlist): song_dict[artist_item] = song_dict.get(artist_item, [])+[playlist_item]
    for key, val in song_dict.items(): random.shuffle(song_dict[key])
    for artist_item, playlist_item in sorted(song_dict.items(), key=lambda x:len(x[1]), reverse=True):
        interval = (len(artist)//len(playlist_item), len(artist)//len(playlist_item)-1 if len(artist)//len(playlist_item)-1>=2 else len(artist)//len(playlist_item))
        idx = shuffle_idx.pop(0)
        for playlist_name in playlist_item:
            suffle_list[idx] = playlist_name
            idx += interval[random.randrange(2)]
            while idx not in shuffle_idx: idx+=1
            shuffle_idx.remove(idx)
    print(suffle_list)
    
    

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import numpy as np
from numpy.linalg import norm
from itertools import combinations
num_sim_user_topk = int(input())
num_item_rec_topk = int(input())
num_users = int(input())
num_items = int(input())
num_rows = int(input())
MASK = [[0]*num_items for i in range(num_users)]
def cos_sim(A,B): return np.dot(A,B)/(norm(A)*norm(B))
for i in range(num_rows):
    a, b, c = map(float, sys.stdin.readline().split(' '))
    MASK[int(a-1)][int(b-1)] = c
num_reco_users = int(input())
for i in range(num_reco_users):
    user_list, cos_sim_list = [(range(1,num_users+1))], []
    user = int(input())
    for idx in range(num_users): 
        cos_sim_list.append([cos_sim(np.array(MASK[user-1]), np.array(MASK[idx])), idx+1])
    result = [x[1] for x in sorted(cos_sim_list, key = lambda x:x[0], reverse=True)[1:3]]

    print(result)
    



# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import numpy as np
from numpy.linalg import norm
num_sim_user_topk = int(input())
num_item_rec_topk = int(input())
num_users = int(input())
num_items = int(input())
num_rows = int(input())
MASK = [[0]*num_items for i in range(num_users)]
def cos_sim(A,B): return np.dot(A,B)/(norm(A)*norm(B))
for i in range(num_rows):
    a, b, c = map(float, sys.stdin.readline().split(' '))
    MASK[int(a-1)][int(b-1)] = c
num_reco_users = int(input())
for i in range(num_reco_users):
    user_list, cos_sim_list = [(range(1,num_users+1))], []
    user = int(input())
    for idx in range(num_users): cos_sim_list.append([cos_sim(np.array(MASK[user-1]), np.array(MASK[idx])), idx+1])
    proximity_users = [x[1] for x in sorted(cos_sim_list, key = lambda x:x[0], reverse=True)[1:1+num_sim_user_topk]]
    origin_set, recomand_set, recomand_list = set(), set(), []
    for idx in range(num_items):
        if MASK[user-1][idx] != 0: origin_set.add(idx+1)
    for recomand_user in proximity_users:
        for idx in range(num_items):
            if MASK[recomand_user-1][idx] != 0:
                recomand_set.add(idx+1)
                recomand_list.append([idx, MASK[recomand_user-1][idx]])
    diff_set, result = recomand_set - origin_set, []
    print(recomand_set, diff_set)
    print(sorted(recomand_list,key=lambda x:x[1], reverse=True))
    for idx, val in sorted(recomand_list,key=lambda x:x[1], reverse=True):
        if idx in diff_set: result.append(idx)
        if len(result) >= num_item_rec_topk: break
    print(result)
    

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import codecs
import random
sys.stdin = codecs.getreader("utf-8")(sys.stdin.detach())
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
num = int(input())
for i in range(num):
    playlist = sys.stdin.readline().replace('\n','').split('\t')
    artist = sys.stdin.readline().replace('\n','').split('\t')
    song_dict, shuffle_list, shuffle_idx = dict(), [" "]*len(artist), list(range(len(artist)))
    for artist_item, playlist_item in zip(artist, playlist): song_dict[artist_item] = song_dict.get(artist_item, [])+[playlist_item]
    for key, val in song_dict.items(): random.shuffle(song_dict[key])
    for artist_item, playlist_item in sorted(song_dict.items(), key=lambda x:len(x[1]), reverse=True):
        interval = (len(shuffle_idx)//len(playlist_item), len(shuffle_idx)//len(playlist_item)-1 if len(shuffle_idx)//len(playlist_item)-1>=0 else len(shuffle_idx)//len(playlist_item))
        idx = shuffle_idx.pop(0)
        print(playlist_item)
        for playlist_idx, playlist_name in enumerate(playlist_item):
            shuffle_list[idx] = playlist_name
            if playlist_idx == len(playlist_item)-1: break
            idx += interval[random.randrange(2)]
            while idx not in shuffle_idx:idx+=1
            shuffle_idx.remove(idx)
    print('\t'.join(shuffle_list))




1. 쉬운거.. max 이용
2. 영화추천
3. scatter palindrone
4. 추천