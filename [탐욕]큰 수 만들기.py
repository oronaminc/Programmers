def solution(number, k):
    st = []
    for i in range(len(number)):
        while st and k > 0 and st[-1] < number[i]:
            st.pop()
            k -= 1
        st.append(number[i])
    return ''.join(st[:len(number)-k])



def solution(number, k):
    STACK = []
    for idx, num in enumerate(number):
        while STACK and STACK[-1] < num and k>0:
            STACK.pop()
            k -= 1            
        STACK.append(num)
        if k == 0: break
    return (''.join(STACK)+number[idx+1:])[:len(number)-k]
