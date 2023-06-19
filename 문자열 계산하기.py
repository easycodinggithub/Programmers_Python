def solution(my_string):
    cal = my_string.split(" ")
    count = int(cal[0])
    for i in range(0, len(cal), 1):
        if (cal[i] == '+'):
            count += int(cal[i+1])
        elif (cal[i] == '-'):
            count -= int(cal[i+1])
    return count
            