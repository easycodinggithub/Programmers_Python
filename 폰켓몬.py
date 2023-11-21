def solution(nums):
    limit = len(nums)//2
    answer = len(list(set(nums)))
    if (answer >= limit):
        return limit
    return answer
    