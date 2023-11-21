def solution(a, b):
    day = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    week = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    total = sum(day[0:a-1])+b
    return week[total%7-1]