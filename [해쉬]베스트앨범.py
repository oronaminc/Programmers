def solution(genres, plays):
    COUNT, IDX, answer = dict(), range(len(genres)), []
    for genre, play, idx in zip(genres, plays, IDX): COUNT[genre] = COUNT.get(genre, []) + [[play, idx]]
    for key in COUNT.keys(): COUNT[key].sort(key = lambda x:x[0], reverse=True)
    COUNT = sorted(COUNT.items(), key=lambda x: sum(map(lambda item:item[0], x[1])), reverse=True)
    for genre, play in COUNT:
        if len(play) == 1: answer.append(play[0][1])
        else: answer.extend([play[0][1], play[1][1]])
    return answer

def solution(genres, plays):
    album, album_count = dict(), dict()
    answer, album_idx = [], range(len(genres))
    for genre, play, idx in zip(genres, plays, album_idx):
        album[genre] = album.get(genre, []) + [[play, idx]]
        album_count[genre] = album_count.get(genre, 0) + play
    for key in album.keys(): album[key] = sorted(album[key], key=lambda x : x[0], reverse = True)
    sorted_album_count = sorted(album_count.items(), key = lambda item : item[1], reverse=True)
    for (temp_genre, cnt) in sorted_album_count:
        if len(album[temp_genre][0])==1: answer.append(album[temp_genre][0][1])
        for (temp_play, temp_idx) in album[temp_genre][:2]: answer.append(temp_idx)
    return answer