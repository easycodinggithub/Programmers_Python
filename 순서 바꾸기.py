def solution(num_list, n):
    answer = []
    return num_list[n:len(num_list)] + num_list[0:n]