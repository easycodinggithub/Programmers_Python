def solution(array):
    answer = ""
    count = 0
    for i in array:
        answer += str(i)
    for j in list(answer):
        if (j == str(7)):
            count += 1
    return count