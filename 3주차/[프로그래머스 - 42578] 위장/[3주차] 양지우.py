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
