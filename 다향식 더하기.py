def solution(polynomial):
    answer = polynomial.split(" + ")
    x = 0
    n = 0
    final = []
    for i in answer:
        if (i == 'x'):
            x += 1   
        elif (i.find('x') != -1):
            x += int(i[0:-1])
        else:
            n += int(i)
    if (x == 1):
        final.append('x')
    elif (x > 1):
        final.append(str(x)+'x')
    
    if (n > 0):
        final.append(str(n))
        
    return " + ".join(final)