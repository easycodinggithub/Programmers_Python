def solution(numbers):
    answer = []
    for i in range(0, len(numbers), 1):
        for j in range(0, len(numbers), 1):
            if (i != j):
                answer.append(numbers[i]+numbers[j])
    return sorted(list(set(answer)))