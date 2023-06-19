def solution(my_strings, parts):
    answer = []
    for i in range(0, len(my_strings), 1):
        index0 = parts[i][0]
        index1 = parts[i][1]
        result = (my_strings[i])[index0:index1+1]
        answer.append(result)
    return "".join(answer)