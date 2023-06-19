def solution(numbers, k):
    i = 0
    while True:
        print(i)
        if (k <= 1):
            break
        if (i == len(numbers)-2):
            i = 0
        elif (i == len(numbers)-1):
            i = 1
        else:
            i += 2
        k -= 1
    return numbers[i]