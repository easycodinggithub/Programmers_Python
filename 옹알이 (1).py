def solution(babbling):
    answer = ["aya", "ye", "woo", "ma"]
    count = 0
    index = 0
    for i in range(0, len(babbling), 1):
        for j in answer:
            index = str(babbling[i]).find(j)
            if(index > -1):
                babbling[i] = babbling[i].replace(j, "0")
    
    for i in babbling:
        for j in range(10):
            if (i == "0"*(j+1)):
                count += 1
    return count