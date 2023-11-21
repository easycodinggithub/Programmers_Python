def solution(s):
    answer = True
    psum = 0
    ysum = 0
    
    for i in list(s):
        if (i == 'p' or i == 'P'):
            psum += 1
        elif (i == 'y' or i == 'Y'):
            ysum += 1
    if (psum == ysum):
        return True
    else:
        return False