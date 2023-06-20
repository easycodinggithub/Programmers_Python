def solution(str_list):
    if (len(str_list) == 1):
        return []
    for i in range(0, len(str_list), 1):
        if (str_list[i] == 'l'):
            return str_list[0:i]
        elif (str_list[i] == 'r'):
            return str_list[i+1:len(str_list)+1]