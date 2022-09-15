def solution(clothes):
    arr={}
    for i in range(len(clothes)):
        if clothes[i][1] in arr:
            arr[clothes[i][1]].append(clothes[i][0])
        else:
            arr[clothes[i][1]]=[clothes[i][0]]
    answer=1
    for i in arr.values():
        answer*=(len(i)+1)
    return answer-1


# 좋은 풀이
def solution(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer
