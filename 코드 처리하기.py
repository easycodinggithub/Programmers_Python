def solution(code):
    mode = 0
    ret = []
    for i in range(0, len(code), 1):
        if (mode == 0):
            if (code[i] == "1"):
                mode = 1
            else:
                if (i % 2 == 0):
                    ret.append(code[i])         
        else:
            if (code[i] == "1"):
                mode = 0
            else:
                if (i % 2 == 1):
                    ret.append(code[i])
    if (len(ret) == 0):
        return "EMPTY"
    return "".join(ret)