from collections import Counter
def solution(array):
    print(Counter(array).most_common())
    most = Counter(array).most_common(2)
    if (len(most) <= 1):
        return most[0][0]
    elif (most[0][1] == most[1][1]):
        return -1
    else:
        return most[0][0]