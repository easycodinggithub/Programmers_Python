def solution(my_string, m, c):
    answer = []
    for i in range(0, len(my_string)//m, 1):
        answer.append(my_string[i*m+c-1])
            
    return "".join(answer)