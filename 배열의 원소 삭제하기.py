def solution(arr, delete_list):
    answer = []
    for i in arr:
        check = 0
        for j in delete_list:
            if (i == j):
                check = 1
        if (check == 0):
            answer.append(i)
    return answer