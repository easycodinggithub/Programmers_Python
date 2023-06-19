def solution(my_string, queries):
    my_list = list(my_string)
    for i in queries:
        subArr = [my_list[k] for k in range(i[1], i[0]-1, -1)]
        index = 0
        for j in range(i[0], i[1]+1, 1):
            my_list[j] = subArr[index]
            index += 1
    return "".join(my_list)