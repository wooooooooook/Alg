
def push(arr, value):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < value:
            left = mid + 1
        else:
            right = mid
    arr.insert(left, value)


def solution(operations: list) -> list:
    lit = []
    for i in operations:
        if "I" in i:
            push(lit, int(i[2:]))
        elif lit and i[2] == "-":
            lit.pop(0)
        elif lit:
            lit.pop()
    if not lit:
        return [0, 0]
    if len(lit) == 1:
        return [lit[0], lit[0]]
    return [lit.pop(), lit.pop(0)]
