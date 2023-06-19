def solution(a, b, c, d):
    if (a == b and b == c and c == d):
        return 1111*a
    elif (a == b and b == c and c != d):
        return (10*a+d)*(10*a+d)
    elif (a == b and b != c and b == d):
        return (10*a+c)*(10*a+c)
    elif (a != b and a == c and c == d):
        return (10*a+b)*(10*a+b)
    elif (a != b and b == c and c == d):
        return (10*b+a)*(10*b+a)
    elif (a == b and c == d):
        return (b+c)*abs((b-c))
    elif (a == c and b == d):
        return (c+b)*abs((c-b))
    elif (a == d and c == b):
        return (d+c)*abs((d-c))
    elif (a == b):
        return c*d
    elif (a == c):
        return b*d
    elif (a == d):
        return b*c
    elif (b == c):
        return a*d
    elif (b == d):
        return a*c
    elif (c == d):
        return a*b
    else:
        return min([a, b, c, d])
    
    
    