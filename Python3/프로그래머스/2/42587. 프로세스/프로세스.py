def solution(priorities: list, location: int) -> int:
    pointer, timing = 0, 1
    output = [0] * len(priorities)
    index = priorities.copy()
    mx = max(index)
    while True:
        if priorities[pointer] == mx:
            output[pointer] = timing
            timing += 1
            index.remove(mx)
            if len(index) == 0:
                break
            mx = max(index)
        pointer = (pointer + 1) % len(priorities)
    return output[location]
