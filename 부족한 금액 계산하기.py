def solution(price, money, count):
    sum = 0
    for i in range(1, count+1, 1):
        sum += price * i
    if (sum - money <= 0):
        return 0
    return sum - money