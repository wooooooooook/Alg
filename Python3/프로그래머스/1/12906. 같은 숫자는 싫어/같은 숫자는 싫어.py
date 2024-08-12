def solution(arr):
    last = -1
    output = []
    for i in arr:
        if i != last:
            output.append(i)
        last = i
    return output