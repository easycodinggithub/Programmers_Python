def solution(my_string, s, e):
    my_list = list(my_string)
    my_list2 = my_list[s:e+1]
    if (len(my_list2) <= 0):
        return my_list
    print(my_list2)
    index = len(my_list2)-1
    for i in range(s, e+1, 1):
        my_list[i] = my_list2[index]
        index -= 1
    return "".join(my_list)