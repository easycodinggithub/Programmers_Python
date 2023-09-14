def solution(brown, yellow):
    size = brown + yellow
    for i in range(1, brown//2, 1):
        for j in range(1, brown//2, 1):
            if i * j == size and i >= j and j >= 3 and (i*2+j*2)-4 == brown:
                return([i, j])