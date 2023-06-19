import re
def solution(my_string):
    n = re.split("[a-zA-Z]", my_string)
    count = 0
    for i in n:
        if (i != ''):
            count += int(i)
    return count