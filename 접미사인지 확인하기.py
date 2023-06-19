def solution(my_string, is_suffix):
    for i in range(0, len(my_string), 1):
        print(my_string[i:len(my_string)])
        if (my_string[i:len(my_string)] == is_suffix):
            return 1
    return 0