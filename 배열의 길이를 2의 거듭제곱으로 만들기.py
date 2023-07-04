def solution(arr):
    count = 1
    while True:
        if (len(arr) <= count):
            for i in range(count-len(arr)):
                arr.append(0)
            return arr
        count *= 2
        
        