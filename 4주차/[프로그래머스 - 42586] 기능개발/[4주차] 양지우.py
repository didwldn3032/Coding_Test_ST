import math
def solution(progresses, speeds):
    answer = []
    max=0
    cnt=0
    for i in range(len(progresses)):
        num=math.ceil((100-progresses[i])/speeds[i])
        print(num,max)
        if max>=num:
            cnt+=1
        else:
            max=num
            answer.append(cnt)
            cnt=1
    answer.append(cnt)

    return answer[1:]
