def solution(my_string):
    answer = []
    for i in list(my_string):
        print(("".join(i)).upper())
        if (i == "".join(i).upper()):
            answer.append("".join(i).lower())
        else:
            answer.append("".join(i).upper())
    return "".join(answer)