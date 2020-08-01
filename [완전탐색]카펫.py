def solution(brown, red):
    square_val, plus_val = brown+red, brown//2+2
    for num in range(3, plus_val-2):
        if num * (plus_val-num) == square_val: return [plus_val-num, num]