from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    wating =  deque(truck_weights)
    bridge = deque([0 for _ in range(bridge_length)])
    bridgeWeight = 0
    while len(wating) or bridgeWeight > 0:
        remove_truck = bridge.popleft()
        bridgeWeight -= remove_truck

        if len(wating) and bridgeWeight + wating[0] <= weight:
            new_truck = wating.popleft()
            bridgeWeight += new_truck

            bridge.append(new_truck)
        else:
            bridge.append(0)
        time += 1
    return time