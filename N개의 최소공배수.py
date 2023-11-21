def solution(arr):
    i = 1
    while True:
        check = 0
        for j in arr:
            if i % j == 0:
                check += 1
        if check == len(arr):
            return i
        i += 1
        
                