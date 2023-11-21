def solution(X, Y):
    arrX = list(X)
    arrY = list(Y)
    arrXcount = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    arrYcount = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    answer = []
    for i in arrX:
        arrXcount[int(i)] += 1
    for i in arrY:
        arrYcount[int(i)] += 1
    for i in range(0, 10, 1):
        if arrXcount[i] > 0 and arrYcount[i] > 0:
            for j in range(min([arrXcount[i], arrYcount[i]])):
                answer.append(str(i))
    answer = sorted(answer, reverse=True)
    if len(answer) <= 0:
        return "-1"
    elif answer[0] == "0":
        return "0"
    return "".join(answer)