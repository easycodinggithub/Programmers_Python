def solution(a, b, c):
    if (a == b and b == c):
        return (3*a)*(3*a*a)*(3*a*a*a)
    elif (a == b or a == c or b == c):
        return (a+b+c)*(a*a+b*b+c*c)
    else:
        return a+b+c