from collections import deque


def solution(bridge_length: int, weight: int, truck_weights: list) -> int:
    tick, cur_weight, count = 0, 0, 0
    bridge = deque([0] * bridge_length)
    limit = len(truck_weights)
    while True:
        if count == limit:
            break
        output = bridge.popleft()
        if output != 0:
            cur_weight -= output
            count += 1
        try:
            if cur_weight + truck_weights[0] <= weight:
                cur_weight += truck_weights[0]
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)
        except IndexError:
            bridge.append(0)
        tick += 1
    return tick
