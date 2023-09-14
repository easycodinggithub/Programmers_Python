def solution(s):
    ss = s.split(" ")
    result = []
    for i in ss:
        if i == "":
            result.append("")
        elif len(i) == 1:
            result.append(i.upper())
        elif i[0].isdigit():
            result.append(i[0]+i[1:].lower())
        else:
            result.append(i[0].upper()+i[1:].lower())
    return " ".join(result)