def solution(my_string):
    count = 0
    for i in my_string:
        if (i.isdigit()):
            count += int(i)
    return count