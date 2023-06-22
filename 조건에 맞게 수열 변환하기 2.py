def solution(arr):
    counts = 0
    while True:
        answer = []
        count = 0
        for i in arr:
            if (i >= 50 and i % 2 == 0):
                answer.append(i//2)
            elif (i < 50 and i % 2 == 1):
                answer.append(i*2+1)
            else:
                count += 1
        if (count == len(arr)):
            return counts
        else:
            arr = answer
        counts += 1