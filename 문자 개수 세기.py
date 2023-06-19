def solution(my_string):
    lower = [0 for i in range(26)]
    upper = [0 for i in range(26)]
    for i in my_string:
        if (i.islower() == True):
            lower[ord(i)-97] += 1
        else:
            upper[ord(i)-65] += 1
    return upper+lower