def solution(my_string):
    eng = ['a', 'e', 'i', 'o', 'u']
    answer = []
    for i in list(my_string):
        if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
            continue
        answer.append(i)
    return "".join(answer)