import collections

def solution(participant, completion):
    answer = list(collections.Counter(participant)-collections.Counter(completion))[0]
    return answer
