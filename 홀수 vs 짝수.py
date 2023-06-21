def solution(num_list):
    odd = 0
    even = 0
    for i in range(0, len(num_list), 1):
        if (i % 2 == 0):
            even += num_list[i]
        else:
            odd += num_list[i]
    return max([odd, even])
        