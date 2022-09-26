def solution(bridge_length, weight, truck_weights):
    bridge=[]
    answer = 0
    while truck_weights:
        if len(bridge)==bridge_length:
            bridge.pop(0)
        if (sum(bridge)+truck_weights[0]<=weight) and(len(bridge)<bridge_length):
            bridge.append(truck_weights[0])
            truck_weights.pop(0)
        elif len(bridge)<bridge_length:
            bridge.append(0)
        answer+=1
    return answer+bridge_length
