def solution(my_string, is_prefix):
    for i in range(0, len(my_string), 1):
        if (my_string[:i] == is_prefix):
            return 1
    return 0