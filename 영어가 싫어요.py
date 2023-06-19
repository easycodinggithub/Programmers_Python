def solution(numbers):
    answer = ["zero", "one", "two", "three", "four", "five", 
              "six", "seven", "eight", "nine"]
    for i in range(0, len(answer), 1):
        numbers = numbers.replace(answer[i], str(i))
    return int(numbers)