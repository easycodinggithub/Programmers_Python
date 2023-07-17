def solution(seoul):
    answer1 = "김서방은 "
    answer2 = "에 있다"
    for i in range(0, len(seoul), 1): 
        if (seoul[i] == "Kim"):
            return answer1 + str(i) + answer2