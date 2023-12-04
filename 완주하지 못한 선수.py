from collections import Counter 

def solution(participant, completion):
    part = Counter(participant)
    com = Counter(completion)

    part.subtract(com)

    return ''.join(list(part.elements())) 