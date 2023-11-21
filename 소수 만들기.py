def solution(nums):
    prime = []
    answer = 0
    for i in range(0, len(nums), 1):
        for j in range(i+1, len(nums), 1):
            for k in range(j+1, len(nums), 1):
                prime.append(nums[i]+nums[j]+nums[k])
    for i in prime:
        check = 0
        for j in range(2, i, 1):
            if (i % j == 0):
                check = 1
                break
        if (check == 0):
            answer += 1
    return answer
                    