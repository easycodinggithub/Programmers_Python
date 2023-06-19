def solution(emergency):
    nums = sorted(emergency, reverse = True)
    answer = []
    for i in emergency:
        for j in range(0, len(nums), 1):
            if (i == nums[j]):
                answer.append(j+1)  
    return answer