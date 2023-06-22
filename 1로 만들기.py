def solution(num_list):
    sum = 0
    for i in num_list:
        sum += divnum(i)
    return sum
    
def divnum(i):
    if (i == 1):
        return 0
    
    if (i % 2 == 0):
        return 1 + divnum(i//2)
    else:
        return 1 + divnum((i-1)//2)