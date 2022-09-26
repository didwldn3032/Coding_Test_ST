from collections import deque
def solution(prices):
    answer = []
    prices=deque(prices)
    while prices:
        cnt=0
        price=prices.popleft()
        for i in prices:
            cnt+=1
            if price>i:
                break
        answer.append(cnt)      
    return answer



## 참고
def solution(prices):
    stack = []
    answer = [0] * len(prices)
    for i in range(len(prices)):
        if stack != []:
            while stack != [] and stack[-1][1] > prices[i]:
                past, _ = stack.pop()
                answer[past] = i - past
        stack.append([i, prices[i]])
    for i, s in stack:
        answer[i] = len(prices) - 1 - i
    return answer
