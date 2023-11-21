def solution(s):
    answer = s
    word = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i in range(0, len(word), 1):
        if answer.find(word[i]) != -1:
            answer = answer.replace(word[i], str(i))
    return int(answer)