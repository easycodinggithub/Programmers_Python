def solution(binomial):
    answer = binomial.split(' ')
    x = int(answer[0])
    y = int(answer[2])
    if (answer[1] == '+'):
        return x+y
    elif (answer[1] == '-'):
        return x-y
    else:
        return x*y