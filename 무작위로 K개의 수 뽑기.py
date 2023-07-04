def solution(arr, k):
    answer = list(dict.fromkeys(arr))
    if (len(answer) < k):
        return answer + ([-1]*(k-len(answer)))
    elif (len(answer) == k):
        return answer
    else:
        return answer[:k]