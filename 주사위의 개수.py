def solution(box, n):
    return (((box[0]//n)*n)*((box[1]//n)*n)*((box[2]//n)*n))//(n*n*n)