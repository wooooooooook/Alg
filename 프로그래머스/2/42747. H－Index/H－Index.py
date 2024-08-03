
def solution(citations: list) -> int:
    citations.sort()
    pointer = len(citations)
    while 1:
        pointer -= 1
        if pointer == 0 or citations[pointer-1] < len(citations[pointer-1:]):
            break
    h = citations[pointer]
    while 1:
        if h <= len(citations[pointer:]):
            break
        h -= 1
    return h
