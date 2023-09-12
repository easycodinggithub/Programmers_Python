def solution(arr, divisor):
    solution = []
    for i in arr:
        if i % divisor == 0:
            solution.append(i)
    if len(solution) <= 0:
        solution.append(-1)
    return sorted(solution)