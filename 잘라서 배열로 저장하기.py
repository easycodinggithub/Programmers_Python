import math
def solution(my_str, n):
    answer = []
    print(math.ceil(len(my_str)/n))
    for i in range(0, math.ceil(len(my_str)/n), 1):
        answer.append(my_str[i*n:(i+1)*n])
    return answer