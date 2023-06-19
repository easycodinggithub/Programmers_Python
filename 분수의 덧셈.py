import math
def solution(numer1, denom1, numer2, denom2):
    number = denom1*numer2+denom2*numer1
    demon = denom1*denom2
    gcd = math.gcd(number, demon)
    return [number//gcd, demon//gcd]