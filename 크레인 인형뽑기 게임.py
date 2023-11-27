def solution(board, moves):
    answer = []
    for i in moves:
        for j in range(0, len(board), 1):
            if board[j][i-1] > 0:
                answer.append(board[j][i-1])
                board[j][i-1] = 0
                break
    count = 0
    i = 0
    while True:
        if answer[i] == answer[i+1]:
            del answer[i]
            del answer[i]
            count += 2
            i = -1
        if i >= len(answer)-2:
            break
        i += 1
    return count
                