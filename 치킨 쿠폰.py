import sys

def solution(chicken):
    global answer
    answer = 0
    getchicken(chicken)
    return(answer)
    
def getchicken(chicken):
    global answer
    if (chicken < 10):
        return chicken
    print("치킨", chicken//10)
    answer += chicken//10
    return chicken + getchicken((getcoupon(chicken)+chicken//10))
def getcoupon(chicken):
    print("쿠폰",chicken%10)
    return chicken % 10