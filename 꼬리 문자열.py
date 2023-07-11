def solution(str_list, ex):
    answer = []
    for i in str_list:
        if (i.find(ex) < 0):
            answer.append(i)
    return "".join(answer)