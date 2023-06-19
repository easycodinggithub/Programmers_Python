def solution(arr, query):
    answer = arr
    for i in range(0, len(query), 1):
        if (i % 2 == 0):
            answer = answer[0:query[i]+1]
        else:
            answer = answer[query[i]:len(answer)]
    return answer