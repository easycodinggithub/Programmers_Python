def solution(lottos, win_nums):
    win = 0 
    tie = lottos.count(0)
    answer = []
    for i in lottos:
        for j in win_nums:
            if (i != 0 and i == j):
                win += 1
                break
    if (win+tie < 2):
        answer.append(6)
    else:
        answer.append(7-(win+tie))
    if (win < 2):
        answer.append(6)
    else:
        answer.append(7-win)
    return answer    
