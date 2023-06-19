def solution(numbers, direction):
    if (direction == "left"):
        outside = 0
        inside = len(numbers)-1
    else:
        outside = len(numbers)-1
        inside = 0

    num = numbers[outside]    
    del numbers[outside]
    numbers.insert(inside, num)
    return numbers