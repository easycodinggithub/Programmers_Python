def solution(order):
    nums = list(str(order))
    count = 0
    for i in nums:
        if ((int(i) == 3) or (int(i) == 6) or (int(i) == 9)):
            count += 1
    return count