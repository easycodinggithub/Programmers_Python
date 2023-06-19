import math

def solution(balls, share):
    return (f(balls))/(f(balls-share)*f(share))

def f(n):
    return math.factorial(n)