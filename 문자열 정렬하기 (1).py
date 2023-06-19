def solution(my_string):
    string = []
    for i in list(my_string):
        if (i == "0" or ((ord(i) >= 49) and (ord(i) <= 57))):
            string.append(int(i))
    answer = sorted(string)
    return answer