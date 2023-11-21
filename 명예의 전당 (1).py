def solution(k, score):
    stage = []
    answer = []
    for i in score:
        stage.append(i)
        stage = sorted(stage, reverse=True)
        if (len(stage) < k):
            answer.append(stage[-1])
        else:
            answer.append(min(stage[0:k]))
    return answer