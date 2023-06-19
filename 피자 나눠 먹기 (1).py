def solution(n):
    pizza = [ i for i in range(7, 106, 7) ]
    print(99//7)
    for j in pizza:
        if (n <= j):
            return j/7