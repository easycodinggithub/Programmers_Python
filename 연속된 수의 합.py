def solution(num, total):
    if (total == 0):
        numlist = [i for i in range(num*-1, num+1, 1)]
    else:
        numlist = [i for i in range(num*total*-1, num*total+1, 1)]
    for i in range(0, len(numlist)-num+1, 1):
        if (sum(numlist[i:i+num]) == total):
            return numlist[i:i+num]