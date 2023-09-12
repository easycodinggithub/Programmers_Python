def solution(phone_number):
    start = len(phone_number)-4
    end = start + 4
    answer = ("*" * start) + phone_number[start:end]
    return answer